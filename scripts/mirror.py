#!/usr/bin/env python3
"""把 GitHub 主页 README 镜像成博客上的一页：matsuri.site/github/，给国内打不开 GitHub 的人看。

做的事：
- 图片和视频全部搬到本站（raw.githubusercontent.com 和 user-attachments 在国内基本打不开）
- 用 marked（GFM）把 README 渲染成 HTML，套一个浅色页面
- 写进 --out 指定的目录（可以给多个）

GitHub 附件视频不登录下载不了：本机用 --video 网址=本机文件 给成片；
CI 上没有成片，就沿用 --out 目录里上次已经搬过去的同名文件（video-<附件号前 8 位>.mp4）。

本机由 ~/.local/bin/readme-mirror 调用；仓库里 .github/workflows/mirror.yml 在 README 改动后自动跑。
"""
import argparse
import html
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

PAGE = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>马自立 · 项目主页</title>
<meta name="description" content="GitHub 主页 github.com/MatsuriMW 的国内镜像：Obsidian 插件、AI Skill、舆情研判工作流等项目。">
<style>
:root { color-scheme: light; --page:#f6f5f1; --surface:#fcfcfb; --ink:#1f1f1d; --ink-2:#55544f; --ink-3:#8a8984; --rule:#e6e4de; --blue:#2a78d6; }
* { box-sizing: border-box; }
body { margin:0; background:var(--page); color:var(--ink); font:16px/1.75 -apple-system,"PingFang SC","Hiragino Sans GB","Noto Sans SC","Microsoft YaHei",sans-serif; }
.wrap { max-width: 920px; margin: 0 auto; padding: 24px 24px 72px; }
@media (max-width:520px) { .wrap { padding: 16px 16px 56px; } }
.mirror { font-size:13px; color:var(--ink-2); background:var(--surface); border:1px solid var(--rule); border-radius:8px; padding:8px 14px; margin-bottom:20px; }
.mirror a, .md a { color:var(--blue); text-decoration:none; }
.md { background:var(--surface); border:1px solid var(--rule); border-radius:12px; padding:20px 28px 28px; }
@media (max-width:520px) { .md { padding: 12px 14px 20px; } }
.md img, .md video { max-width:100%; height:auto; }
.md video { display:block; margin: 8px auto 20px; border-radius:8px; background:#000; }
.md h2 { font-size:21px; margin:32px 0 10px; padding-bottom:6px; border-bottom:1px solid var(--rule); }
.md table { border-collapse:collapse; margin:12px auto; font-size:14px; }
.md .scroll { overflow-x:auto; }
.md th, .md td { border:1px solid var(--rule); padding:6px 10px; vertical-align:top; }
.md th { background:#f3f2ee; font-weight:600; }
.md td img { display:block; margin:0 auto; }
.md p[align=center], .md td[align=center] { text-align:center; }
.md ul { padding-left:22px; }
footer { margin-top:24px; font-size:12px; color:var(--ink-3); text-align:center; }
</style></head><body><div class="wrap">
<div class="mirror">这是 GitHub 主页 <a href="https://github.com/MatsuriMW">github.com/MatsuriMW</a> 的镜像，内容和图片同步自那边的 README，方便打不开 GitHub 时看。项目链接仍然指向 GitHub。同步于 {date}。</div>
<div class="md">
{body}
</div>
<footer>马自立</footer>
</div></body></html>
'''

ATTACHMENT = re.compile(r'https://github\.com/user-attachments/assets/[0-9a-f-]+')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=str(Path(__file__).resolve().parent.parent), help='主页 README 所在的仓库')
    ap.add_argument('--out', action='append', required=True, help='输出目录（…/github），可以给多个')
    ap.add_argument('--video', action='append', default=[], help='附件网址=本机文件')
    args = ap.parse_args()

    repo = Path(args.repo)
    outs = [Path(o) for o in args.out]
    videos = dict(v.split('=', 1) for v in args.video)
    md = (repo / 'README.md').read_text(encoding='utf-8')
    build = Path(tempfile.mkdtemp())
    assets = build / 'assets'
    assets.mkdir()

    # 视频：附件地址换成本站的 <video>；本机给了成片用成片，没给就沿用上次搬过去的
    for url in sorted(set(ATTACHMENT.findall(md))):
        name = 'video-' + url.rstrip('/').split('/')[-1][:8] + '.mp4'
        src = Path(videos[url]) if url in videos else next((o / 'assets' / name for o in outs if (o / 'assets' / name).exists()), None)
        if not src or not src.exists():
            sys.exit(f'视频 {url} 没有本机成片，本站也还没有 {name}：在本机跑一次 readme-mirror --push，并在它的 VIDEOS 里配上成片')
        shutil.copy(src, assets / name)
        md = md.replace(url, f'<video controls preload="metadata" playsinline src="assets/{name}"></video>')

    # 图片：仓库里的直接拷，远程的下载下来
    def localize(m):
        src = m.group(1)
        if src.startswith('assets/') and (assets / Path(src).name).exists():
            return m.group(0)
        if src.startswith('assets/'):
            shutil.copy(repo / src, assets / Path(src).name)
            return f'src="assets/{Path(src).name}"'
        if src.startswith('http'):
            parts = src.rstrip('/').split('/')
            name = f'{parts[4]}-{parts[-1]}' if 'raw.githubusercontent.com' in src else parts[-1]
            with urllib.request.urlopen(src, timeout=60) as r:
                (assets / name).write_bytes(r.read())
            return f'src="assets/{name}"'
        return m.group(0)
    md = re.sub(r'src="([^"]+)"', localize, md)
    leftover = re.findall(r'https://(?:raw\.githubusercontent\.com|github\.com/user-attachments)\S+', md)
    if leftover:
        sys.exit(f'还有没搬到本站的资源：{leftover}')

    src_md = build / 'README.md'
    src_md.write_text(md, encoding='utf-8')
    body = subprocess.run(['npx', '-y', 'marked@12.0.2', '--gfm', '-i', str(src_md)],
                          check=True, capture_output=True, text=True).stdout
    body = re.sub(r'<table>(.*?)</table>', r'<div class="scroll"><table>\1</table></div>', body, flags=re.S)
    date = subprocess.run(['git', '-C', str(repo), 'log', '-1', '--format=%cd', '--date=format:%Y-%m-%d'],
                          capture_output=True, text=True).stdout.strip()
    page = PAGE.replace('{date}', html.escape(date)).replace('{body}', body)

    for t in outs:
        if t.exists():
            shutil.rmtree(t)
        shutil.copytree(assets, t / 'assets')
        (t / 'index.html').write_text(page, encoding='utf-8')
        print(f'写入 {t}')


if __name__ == '__main__':
    main()
