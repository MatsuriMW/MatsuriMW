<p align="center">
  <img src="assets/header.svg" width="840" alt="马自立：用 Agent 把想法做成能用的东西">
</p>

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/MatsuriMW/token-receipt"><img src="assets/token-receipt.svg" width="228" height="440" alt="Token 小票：一天的 token 用量从热敏打印机里打出来"></a></td>
    <td align="center"><a href="https://github.com/MatsuriMW/nautilus-spiral"><img src="assets/nautilus-spiral.gif" width="282" height="440" alt="螺旋日程：鼠标划过螺旋，上方显示那一段做了什么"></a></td>
    <td align="center"><a href="https://github.com/MatsuriMW/telegram-companion"><img src="https://raw.githubusercontent.com/MatsuriMW/telegram-companion/main/docs/images/chat.jpg" width="203" height="440" alt="Telegram Companion：让它夸夸我，它拿日记里当天做的事来夸"></a></td>
  </tr>
  <tr>
    <td align="center">🧾 Token 小票</td>
    <td align="center">🌀 螺旋日程</td>
    <td align="center">💬 Telegram Companion</td>
  </tr>
</table>

<p align="center">🌀 <a href="https://github.com/MatsuriMW/nautilus-spiral">螺旋日程</a> · 50 秒介绍片（有声音）：片子里的面板是插件自己的代码按一篇虚构日记画出来的</p>

https://github.com/user-attachments/assets/1e0967bc-d498-456a-9d82-46750d761c08

<p align="center">🌀 螺旋日程 · 日记里每一行 DOING 下面，实时显示它绑着的 Agent 会话在跑还是在等你、最近一步、用了多少 token，派出去的 subagent 和开着的 side chat 也在这里</p>

<p align="center">
  <a href="https://github.com/MatsuriMW/nautilus-spiral"><img src="https://raw.githubusercontent.com/MatsuriMW/nautilus-spiral/main/assets/agent-lines.gif" width="800" alt="日记里四行 DOING 的任务，每行下面一条等宽字符的进度：监听 Claude · 在跑 · 最近一步 · token；其中一行下面还有一行「side chat · 开着 · 8m」"></a>
</p>

<p align="center">🛰 <a href="https://github.com/MatsuriMW/obsidian-agent-deck">Agent Deck（智能体甲板）</a> · 25 秒演示：把散在各个客户端里的 AI Agent 会话收到一张甲板上，活从笔记里派出去，进度和结果回到笔记里</p>

<p align="center">
  <a href="https://github.com/MatsuriMW/obsidian-agent-deck"><img src="assets/agent-deck.gif" width="800" alt="Agent Deck 演示：会话卡片拖到日记里的任务上绑定，任务拖到 Agent 上委派，状态和结论写回日记"></a>
</p>

## 这些项目拼在一起

想做成的是「文件系统 + Agent」：主库就是一个 Markdown 文件夹，用 Git 管版本；Claude、Pi、Codex、WorkBuddy 读写的是同一个库。工作记录一半由人主动写，一半由 AI 自动记进日记；同一份日记既是陪伴 Agent 回话前读的上下文，也是个人的任务管理。下面的插件和 Skill 都是从这套东西里拆出来的零件。

## Claude 相关：Mod 和 Skill

### 🗂 [Outline Sidebar](https://github.com/MatsuriMW/outline-sidebar)：Claude Code mod，一次 harness 工程实践

AI 时代，人的注意力成了瓶颈。活儿大多交给 Agent 去干，人负责 review；而一场长会话最容易把「装着问题的注意力」切碎：结论、要我拍板的事、交代出去的活、已经做完的事全搅在一条只往下长的流里，回头找要一路往上翻。

Outline Sidebar 把一场 Claude Code 会话整理成 Logseq 式的可折叠大纲侧栏：一轮一块，顺着话题深入是子块，按「结论 / 需要我做的 / 我让它做的 / 它已做的 / 技术信息」分视图过滤。

<p align="center">
  <a href="https://github.com/MatsuriMW/outline-sidebar"><img src="https://raw.githubusercontent.com/MatsuriMW/outline-sidebar/main/docs/outline-sidebar.png" width="800" alt="Outline Sidebar：左边「我让它做的」，每件事带着原话、做成几件、有几件有证据和结论；右边「它已做的」，每条下面挂着改了哪个文件、跑了哪条命令和结果"></a>
</p>

大多数 harness 管的是 Agent 那一侧：给它什么上下文、什么工具、怎么验证它的产出。这个 mod 管的是人那一侧，在 harness 里实际承担两个角色：

1. **可观测性**：结论、要我拍板的事、交代出去的活、它做完的事，分开显示，不用在一条流里往上翻。这直接对着人的瓶颈：review 时的注意力。
2. **结构化的反馈回路**：我在侧栏改的状态会变成结构化信息，传回给 Claude。比如我把「确认仓库是否公开」标成 DONE，Claude 收到的是一条明确的状态变更，用不着再读一段话去猜。人的判断用固定格式回到 Agent 的上下文，这是比较硬的 harness 设计，比聊天里说一句可靠。

为了让 review 看的是证据，而不只是 AI 写的摘要，又加了三样东西：

- **「做了」挂证据**：改了哪些文件、跑了哪些命令、成没成，直接从工具调用里记下来；模型总结时只能从中挑证据，挑不出就标「无证据」
- **验收关口**：待 review 的块要先展开看过证据才能改成 Done，通过时告诉 Claude「用户看过证据后验收」，没证据的条目一并说出来
- **验收没通过，Claude 接着回应**：Rework（要改）、Unclear?（没看懂）、Failed、Errored、Hit Limit!、Suspended、Cancelled 各有一个快捷键。标完停手 4 秒，mod 替我发一条消息，按状态让 Claude 返工、追问、解释或停下；一次打回好几件时，让它把互不相干的交给子代理并行做
- **指标**：证据覆盖率、验收拦下率、返工率、纠正层级，按本次会话和所有会话各算一遍，看这套 harness 到底拦下了多少东西

**目前适配 Claude Code CLI（终端）**，尤其照顾中文输入法：点进侧栏自动切英文键盘，回对话框再切回来；只用方向键和回车也能做完所有操作；图标做成自制字体，和中文对齐。Desktop 版和 VS Code 里能打开，但还很简陋，Desktop 版后面再做。

### Skill

| 项目 | 它做什么 | 现在的状态 |
|---|---|---|
| 🎭 [AI 人物设计 Skill](https://github.com/MatsuriMW/ai-character-design-skill) | 把「轻佻的男性」这种模糊感觉，拆成生图、生视频模型能直接执行的锁定段。附 122 张人物原型卡、服化道和连戏表 | v0.1.3，适用于 Claude Code / Codex / claude.ai |
| 🖼 [角色设定板 + 古典式配图](https://github.com/MatsuriMW/aigc-skills-and-agents) | 两个 Claude Skill：锁定角色长相的三视图和表情板 prompt；版画质感的 SVG 解释图 | 可用 |
| ✍️ [skills-agents-and-prompts](https://github.com/MatsuriMW/skills-agents-and-prompts) | 写稿流水线、带出处的笔记问答、投资调研 Agent、「按感觉找图」等 Skill、Agent 和提示词 | 持续更新 |

## Obsidian 插件

上架 Obsidian 社区插件市场的 5 个插件，在我的[社区主页](https://community.obsidian.md/users/matsurimw)上能一次看全。

| 项目 | 它做什么 | 现在的状态 |
|---|---|---|
| 🌀 [螺旋日程](https://github.com/MatsuriMW/nautilus-spiral) | Obsidian 插件。把今天日记里的事件和待办画成一条螺旋，待办从「现在」往后填进空档，容量条告诉你今天排不排得下；Claude、Codex、WorkBuddy 的会话可以自动记回日记，变成 DOING / SUSPENDED 的任务行和实际时段，任务行下面看得到会话在跑还是在等你、做到了哪一步 | 已上架 Obsidian 社区插件市场，Release 1.7.0，仅桌面端，macOS 上功能最全 |
| 🛰 [Agent Deck（智能体甲板）](https://github.com/MatsuriMW/obsidian-agent-deck) | Obsidian 插件。把散在各个客户端里的 AI Agent 会话收到一张甲板上：哪个 Agent 在干活、哪个在等你、做到了哪一步，抬眼就能看到；要派活，就从笔记里正在写的那一行派出去，进度和结果再回到这一行。人写的计划和 Agent 跑的活，最后落在同一份日记里。[演示片](https://matsuri.site/demo/agent-deck/) | 已上架 Obsidian 社区插件市场，Release 1.2.2，仅桌面端 |
| 🧾 [Token 小票](https://github.com/MatsuriMW/token-receipt) | Obsidian 插件。把一天里 Claude Code、Codex、WorkBuddy 用掉的 token 打成一张购物小票：按模型列出 token 和按 API 标价折算的金额，还有订阅额度用了多少。小票会从热敏打印机里走出来，也能落在木桌、钉上软木板，可以存成图片或会动的 SVG | 已上架 Obsidian 社区插件市场，Release 1.3.1，仅桌面端 |
| 💬 [Telegram Companion](https://github.com/MatsuriMW/telegram-companion) | Obsidian 插件。手机上随手发一句进当天日记；想聊的时候，它先读你近一周的日记再开口。模型自己选，接本机 Ollama 的话日记不出电脑 | 已上架 Obsidian 社区插件市场，Release 1.0.5，GPL-3.0，基于 Telegram Inbox |
| 🔗 [Roam Backlinks](https://github.com/MatsuriMW/roam-backlinks) | Obsidian 插件。像 Logseq、Roam Research 那样在反链里逐块原地编辑，带可展开的面包屑和带反链的 PDF 导出 | 已上架 Obsidian 社区插件市场，Release 1.0.1 |
| 🧰 [Obsidian-Plugins](https://github.com/MatsuriMW/Obsidian-Plugins) | 我自用的全部 Obsidian 插件：本地混合检索的「第二大脑」、LLM Wiki、稿件台、任务归位等。README 里按「装上就能用 / 要配合一套写法 / 适合参考着改」标了推荐度 | 持续更新 |

## 正在做的

- **[Outline Sidebar](https://github.com/MatsuriMW/outline-sidebar)**：证据、验收关口、验收不通过后的自动返工和追问、四个指标都已上线，接下来用几周攒数据，看验收到底拦下了多少；之后做 Desktop 版。
- **第二大脑的检索**：Obsidian-Plugins 里那个本地混合检索（向量 + BM25）。给它建了 48 道题的评测集和 16 道不参与调参的留出题，按 bad case 调了拒答门槛和切块：首条命中 70% → 80%，MRR 0.809 → 0.872，库里没有答案的问题从一道都挡不住到 8 道全部拒答。[在线版](https://matsuri.site/demo/second-brain/)已经上线，补上了生成层：bge-m3 混合检索加重排，DeepSeek 生成，加重排后首条命中率 71% → 85%；44 道应答题忠实度 99%、引用准确率 100%，15 道应拒答题全部拒住。下一步加按日期和文件夹过滤。
- **[小红书舆情研判工作流](https://github.com/MatsuriMW/xhs-yuqing)**：n8n 定时调小红书 MCP 抓品牌相关的笔记和评论，DeepSeek 逐条编码（说的是不是这个品牌、情感、语气、高压线、动员级别、在拿谁做对比），指标由代码算，模型写研判，再用代码规则和另一个模型给研判打分。自动评测之后留一道人工复核，复核出的误判写回配置和编码规则，下一轮自动生效。[Demo](https://matsuri.site/demo/xhs-yuqing/)：特斯拉 Roadster 发布后 24 小时的研判，含人工复核前后的对照。

<p align="center">
  <a href="https://matsuri.site/demo/xhs-yuqing/"><img src="assets/xhs-yuqing-demo.jpg" width="420" alt="舆情研判 demo：特斯拉 Roadster 发布后 24 小时，机器初判和人工复核的对照"></a>
</p>
