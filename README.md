<p align="center">
  <img src="assets/header.svg" width="840" alt="马自立：用 Agent 把想法做成能用的东西">
</p>

<a id="zh" name="zh"></a>
<p align="center"><b>中文</b> · <a href="#english">English</a></p>

<p align="center">想追踪新功能、反馈问题、看我最近的进展，欢迎关注我的 Twitter：<a href="https://x.com/Matsurimywaifu">@Matsurimywaifu</a></p>

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/MatsuriMW/token-receipt"><img src="assets/token-receipt.svg" width="228" height="440" alt="Token 小票：一天的 token 用量从热敏打印机里打出来"></a></td>
    <td align="center"><a href="https://github.com/MatsuriMW/nautilus-spiral"><img src="assets/nautilus-spiral.gif" width="282" height="440" alt="螺旋日程：鼠标划过螺旋，上方显示那一段做了什么"></a></td>
    <td align="center"><a href="https://github.com/MatsuriMW/telegram-companion"><img src="https://raw.githubusercontent.com/MatsuriMW/telegram-companion/main/docs/images/chat.jpg" width="203" height="440" alt="Telegram Companion：让它夸夸我，它拿日记里当天做的事来夸"></a></td>
  </tr>
  <tr>
    <td align="center">🧾 Token 小票<br>Token Receipt</td>
    <td align="center">🌀 螺旋日程<br>Nautilus Spiral</td>
    <td align="center">💬 Telegram Companion</td>
  </tr>
</table>

<p align="center">🌀 <a href="https://github.com/MatsuriMW/nautilus-spiral">螺旋日程</a> · 50 秒介绍片（有声音）：片子里的面板是插件自己的代码按一篇虚构日记画出来的<br>🌀 <a href="https://github.com/MatsuriMW/nautilus-spiral">Nautilus Spiral</a> · 50-second intro (with sound): every panel in it is drawn by the plugin's own code from a made-up journal</p>

https://github.com/user-attachments/assets/1e0967bc-d498-456a-9d82-46750d761c08

<p align="center">🌀 螺旋日程 + 🛰 Agent Deck · 日记里每一行 DOING 下面，实时显示它绑着的 Agent 会话在跑还是在等你、最近一步、用了多少 token，派出去的 subagent 和开着的 side chat 也在这里<br>Nautilus Spiral + Agent Deck · under each DOING line in the journal: whether its agent session is running or waiting for you, the latest step and the tokens used, plus the subagents it sent out and any open side chat</p>

<p align="center">
  <a href="https://github.com/MatsuriMW/nautilus-spiral"><img src="https://raw.githubusercontent.com/MatsuriMW/nautilus-spiral/main/assets/agent-lines.gif" width="800" alt="日记里四行 DOING 的任务，每行下面一条等宽字符的进度：监听 Claude · 在跑 · 最近一步 · token；其中一行下面还有一行「side chat · 开着 · 8m」"></a>
</p>

<p align="center">🛰 <a href="https://github.com/MatsuriMW/obsidian-agent-deck">Agent Deck（智能体甲板）</a> · 25 秒演示：把散在各个客户端里的 AI Agent 会话收到一张甲板上，活从笔记里派出去，进度和结果回到笔记里<br>🛰 <a href="https://github.com/MatsuriMW/obsidian-agent-deck">Agent Deck</a> · 25-second demo: AI agent sessions scattered across apps gathered on one deck; work goes out from your notes, and progress and results come back to them</p>

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

为了让 review 看的是证据，而不只是 AI 写的摘要，又加了这些东西：

- **「做了」挂证据**：改了哪些文件、跑了哪些命令、成没成，直接从工具调用里记下来；模型总结时只能从中挑证据，挑不出就标「无证据」
- **验收关口**：待 review 的块要先展开看过证据才能改成 Done，通过时告诉 Claude「用户看过证据后验收」，没证据的条目一并说出来
- **验收没通过，Claude 接着回应**：Rework（要改）、Unclear?（没看懂）、Failed、Suspended、Cancelled 各有一个快捷键（Errored、Hit Limit! 是 Agent 报给我的，由 mod 自动标）。标完停手 4 秒，mod 替我发一条消息，按状态让 Claude 返工、追问、解释或停下；它问我的问题，按 Y / N 回答，同样直接发过去；一次打回好几件时，让它把互不相干的交给子代理并行做
- **大纲再长也找得到**：顶上一排刻度尺，一轮一格，颜色跟着状态，等我处理的格子更高；还能搜索、多选一起改状态，长期没动的块会提示一键了结
- **指标**：证据覆盖率、验收拦下率、返工率、纠正层级，按本次会话和所有会话各算一遍，看这套 harness 到底拦下了多少东西

**推荐在 Claude Code CLI（终端）里用**，尤其照顾中文输入法：点进侧栏自动切英文键盘，回对话框再切回来；只用方向键和回车也能做完所有操作；图标做成自制字体，和中文对齐。Claude 桌面版的侧栏也调过排版，用鼠标很顺手，键盘操作还是以终端为主；VS Code 里能打开，没专门调过。现在是 0.11.3，正在过 Claude 官方插件目录的审核。

### Skill

| 项目 | 它做什么 | 现在的状态 |
|---|---|---|
| 🎭 [AI 人物设计 Skill](https://github.com/MatsuriMW/ai-character-design-skill) | 把「轻佻的男性」这种模糊感觉，拆成生图、生视频模型能直接执行的锁定段。附 122 张人物原型卡、服化道和连戏表 | v0.1.4，适用于 Claude Code / Codex / claude.ai |
| 🖼 [角色设定板 + 古典式配图](https://github.com/MatsuriMW/aigc-skills-and-agents) | 两个 Claude Skill：锁定角色长相的三视图和表情板 prompt；版画质感的 SVG 解释图 | 可用 |
| ✍️ [skills-agents-and-prompts](https://github.com/MatsuriMW/skills-agents-and-prompts) | 写稿流水线、带出处的笔记问答、投资调研 Agent、「按感觉找图」等 Skill、Agent 和提示词 | 持续更新 |

## Obsidian 插件

上架 Obsidian 社区插件市场的 13 个插件，在我的[社区主页](https://community.obsidian.md/users/matsurimw)上能一次看全。下面先是主打的五个，再是另外八个。

| 项目 | 它做什么 | 现在的状态 |
|---|---|---|
| 🌀 [螺旋日程](https://github.com/MatsuriMW/nautilus-spiral) | Obsidian 插件。把今天日记里的事件和待办画成一条螺旋，待办从「现在」往后填进空档，容量条告诉你今天排不排得下；主线先定目标再开始，进度条能拖，有 macOS 桌面小组件。配上 Agent Deck，AI Agent 的会话也记进日记、画在同一圈螺旋上 | 已上架 Obsidian 社区插件市场，Release 2.2.0，仅桌面端，macOS 上功能最全 |
| 🛰 [Agent Deck（智能体甲板）](https://github.com/MatsuriMW/obsidian-agent-deck) | Obsidian 插件。把散在各个客户端里的 AI Agent 会话收到一张甲板上：哪个 Agent 在干活、哪个在等你、做到了哪一步，抬眼就能看到；要派活，就从笔记里正在写的那一行派出去，进度和结果再回到这一行。人写的计划和 Agent 跑的活，最后落在同一份日记里。[演示片](https://matsuri.site/demo/agent-deck/) | 已上架 Obsidian 社区插件市场，Release 1.2.4，仅桌面端 |
| 🧾 [Token 小票](https://github.com/MatsuriMW/token-receipt) | Obsidian 插件。把一天里 Claude Code、Codex、WorkBuddy 用掉的 token 打成一张购物小票：按模型列出 token 和按 API 标价折算的金额，还有订阅额度用了多少。小票会从热敏打印机里走出来，也能落在木桌、钉上软木板，可以存成图片或会动的 SVG | 已上架 Obsidian 社区插件市场，Release 1.3.1，仅桌面端 |
| 💬 [Telegram Companion](https://github.com/MatsuriMW/telegram-companion) | Obsidian 插件。手机上随手发一句进当天日记；想聊的时候，它先读你近一周的日记再开口，聊完把新知道的事记进一页陪伴档案。模型自己选，接本机 Ollama 的话日记不出电脑 | 已上架 Obsidian 社区插件市场，Release 1.3.0，GPL-3.0，基于 Telegram Inbox |
| 🔗 [Roam Backlinks](https://github.com/MatsuriMW/roam-backlinks) | Obsidian 插件。像 Logseq、Roam Research 那样在反链里逐块原地编辑，带可展开的面包屑和带反链的 PDF 导出；还能按页看反链里的特征词和词对 | 已上架 Obsidian 社区插件市场，Release 1.3.1 |
| 🧰 [Obsidian-Plugins](https://github.com/MatsuriMW/Obsidian-Plugins) | 我自用的全部 Obsidian 插件：本地混合检索的「第二大脑」、LLM Wiki、稿件台、任务归位等。README 里按「装上就能用 / 要配合一套写法 / 适合参考着改」标了推荐度 | 持续更新 |

另外八个，都已上架：

| 插件 | 它做什么 | 版本 |
|---|---|---|
| 🃏 [Card Walk](https://github.com/MatsuriMW/card-walk) | 刷笔记里标了 #card 的问答卡和挖空卡，按 Anki 的间隔排期；手机和电脑都能刷，每次作答同步到了哪一步看得见 | 1.1.0 |
| ✅ [Logseq Style Tasks](https://github.com/MatsuriMW/logseq-style-tasks) | Logseq 式日记里的关键词任务：`todos` 母块、优先级简写、关键词循环组各有快捷键，图标带动画、改状态有音效。基于 TODOseq 改的 | 1.0.0 |
| 🏷 [Logseq Style Alias](https://github.com/MatsuriMW/logseq-style-alias) | 像 Logseq 那样，`[[别名]]` 直接打开带这个别名的页，不会留成空链接或新建一个空页 | 1.0.0 |
| 📁 [Logseq Style Fold](https://github.com/MatsuriMW/logseq-style-fold) | 记住每个列表项的折叠，按 Logseq 的写法把 `collapsed:: true` 写进笔记 | 1.2.0 |
| 🌲 [Emacs Logseq Inspired Outline](https://github.com/MatsuriMW/emacs-logseq-inspired-outline) | 受 Logseq 和 Emacs 启发的大纲编辑：块选择、跳到上级、同级新建、几行归成一组 | 3.3.3 |
| 📑 [Hover Outline](https://github.com/MatsuriMW/hover-outline) | 编辑器角落里藏着一份目录，鼠标移过去才展开 | 1.1.0 |
| 🗂 [Chrome Tab Groups](https://github.com/MatsuriMW/obsidian-chrome-tab-groups) | 像 Chrome 那样给 Obsidian 的标签页分组 | 1.1.3 |
| 🧵 [Thread Studio](https://github.com/MatsuriMW/thread-studio) | 从 Obsidian 笔记写 X 的推文、推文串、长帖和文章。NoteTweet 的改版，经原作者同意发布 | 1.0.0 |

## 正在做的

- **英语备课 Agent**（v0.3.4）：给无锡初中英语老师用的备课 Agent。115 份无锡真卷拆成 4012 个题组；一份教案同时贴合下一场考试、学校、学生的薄弱点和老师的习惯，先出大纲、老师改过再写教案，分老师版和学生版；学生档案是会自己更新的记忆，课后反馈按每位家长的孩子分别写。网页和微信机器人两个入口，我自己做家教备课在用，已在小范围推广。下一步扩到高中和无锡以外的江苏城市：江苏高中英语的卷子和讲义已经整理好，接着建高中的考试结构和题库。[Demo](https://matsuri.site/demo/english-prep/)
- **[Outline Sidebar](https://github.com/MatsuriMW/outline-sidebar)**：证据、验收关口、验收不通过后的自动返工和追问、四个指标、桌面版排版都已上线，现在在过 Claude 官方插件目录的审核；接下来用几周攒数据，看验收到底拦下了多少。
- **第二大脑的检索**：Obsidian-Plugins 里那个本地混合检索（向量 + BM25）。给它建了 48 道题的评测集和 16 道不参与调参的留出题，按 bad case 调了拒答门槛和切块：首条命中 70% → 80%，MRR 0.809 → 0.872，库里没有答案的问题从一道都挡不住到 8 道全部拒答；后来加了按日期过滤，带日期的那组题 MRR 0.85 → 1.0。[在线版](https://matsuri.site/demo/second-brain/)已经上线，补上了生成层：bge-m3 混合检索加重排，DeepSeek 生成，加重排后首条命中率 71% → 85%；44 道应答题忠实度 99%、引用准确率 100%，15 道应拒答题全部拒住。
- **[舆情研判工作流](https://github.com/MatsuriMW/xhs-yuqing)**：先做的是 n8n 版：定时调小红书 MCP 抓品牌相关的笔记和评论，DeepSeek 逐条编码（说的是不是这个品牌、情感、语气、高压线、动员级别、在拿谁做对比），指标由代码算，模型写研判，再用代码规则和另一个模型给研判打分。自动评测之后留一道人工复核，复核出的误判写回配置和编码规则，下一轮自动生效。[Demo](https://matsuri.site/demo/xhs-yuqing/)：特斯拉 Roadster 发布后 24 小时的研判，含人工复核前后的对照。之后换成 LangGraph 编排（仓库里的 `langgraph/`）：同一套编码、指标、规则代码，按品牌人群画像决定以小红书、B站还是知乎为主，先判断是突发事件还是日常，规则没过自动返工，出报告前停下等人复核。[Demo](https://matsuri.site/demo/yuqing-langgraph/)：特斯拉 · B站 + 知乎。

<p align="center">
  <a href="https://matsuri.site/demo/xhs-yuqing/"><img src="assets/xhs-yuqing-demo.jpg" width="420" alt="舆情研判 demo：特斯拉 Roadster 发布后 24 小时，机器初判和人工复核的对照"></a>
</p>

---

<a id="english" name="english"></a>
<p align="center"><a href="#zh">中文</a> · <b>English</b></p>

<p align="center">To follow new features, send feedback or keep up with my recent progress, follow me on Twitter: <a href="https://x.com/Matsurimywaifu">@Matsurimywaifu</a></p>

The demo pages linked below are in Chinese.

## How the pieces fit

What I'm building is "a file system plus agents": my main vault is just a folder of Markdown files under Git, and Claude, Pi, Codex and WorkBuddy all read and write the same vault. Half of the work log I write myself; the other half AI records into my journal. The same journal is the context a companion agent reads before it replies, and it is also my task manager. The plugins and skills below are parts taken out of this setup.

## Claude: a mod and some skills

### 🗂 [Outline Sidebar](https://github.com/MatsuriMW/outline-sidebar): a Claude Code mod, an exercise in harness engineering

With AI doing more of the work, human attention is the bottleneck. Agents do most of the work and people review it, and a long session is exactly what breaks up the attention you bring to a problem: conclusions, decisions waiting on you, tasks you handed off and things already done all end up in one stream that only grows downward, and finding anything means scrolling back up.

Outline Sidebar turns a Claude Code session into a Logseq-style collapsible outline in a sidebar: one block per turn, sub-blocks as a topic goes deeper, and views that filter by Conclusions / Needs me / Asked of it / Done by it / Technical info.

<p align="center">
  <a href="https://github.com/MatsuriMW/outline-sidebar"><img src="https://raw.githubusercontent.com/MatsuriMW/outline-sidebar/main/docs/outline-sidebar.png" width="800" alt="Outline Sidebar: on the left, what I asked it to do, each with my original words, how many got done and how many have evidence and a conclusion; on the right, what it has done, each with the files it changed and the commands it ran and their results"></a>
</p>

Most harnesses work on the agent's side: what context it gets, which tools, how its output gets checked. This mod works on the human side, and plays two roles in the harness:

1. **Observability**: conclusions, decisions waiting on me, tasks I handed off and work it has finished are shown separately, with no scrolling back through one stream. This goes straight at the human bottleneck: attention during review.
2. **A structured feedback loop**: when I change a status in the sidebar, it goes back to Claude as structured information. If I mark "check whether the repo is public" as DONE, Claude gets an explicit status change instead of a paragraph it has to interpret. My judgment returns to the agent's context in a fixed format, which is a firmer piece of harness design than saying it in chat.

So that review looks at evidence and not only at a summary the AI wrote, it also has:

- **Evidence under "done"**: which files changed, which commands ran and whether they worked, recorded straight from the tool calls; when the model summarizes, it can only pick from that evidence, and anything without evidence is marked "no evidence"
- **An acceptance gate**: a block waiting for review can only be marked Done after it has been expanded and its evidence seen; on approval Claude is told "the user accepted this after reviewing the evidence", and items without evidence are named too
- **When a review fails, Claude responds**: Rework, Unclear?, Failed, Suspended and Cancelled each have a hotkey (Errored and Hit Limit! are reported by the agent and marked by the mod). Four seconds after I stop, the mod sends a message for me that tells Claude to redo it, ask, explain or stop, depending on the status. Its questions to me are answered with Y / N and sent the same way. When several items come back at once, it is asked to hand the unrelated ones to subagents in parallel
- **Finding things in a long outline**: a ruler along the top with one tick per turn, colored by status, taller where something is waiting on me; plus search, multi-select to change statuses together, and a nudge to close out blocks that haven't moved in a long time
- **Metrics**: evidence coverage, acceptance rejection rate, rework rate and outline corrections, computed for the current session and across all sessions, to see how much the harness actually catches

**Best in the Claude Code CLI (terminal)**, with care for Chinese input methods: focusing the sidebar switches to an English keyboard and switches back when you return to the prompt; everything can be done with the arrow keys and Enter; the icons are a custom font that lines up with CJK text. The sidebar in Claude Desktop has its own layout and works well with a mouse, though keyboard use is still terminal-first; it opens in VS Code but hasn't been tuned there. It's at 0.11.3 and under review for Claude's official plugin directory.

### Skills

| Project | What it does | Status |
|---|---|---|
| 🎭 [AI Character Design Skill](https://github.com/MatsuriMW/ai-character-design-skill) | Turns a vague impression like "a flippant man" into locked descriptions that image and video models can follow directly. Comes with 122 character archetype cards plus costume, makeup and props notes and continuity sheets | v0.1.4, for Claude Code / Codex / claude.ai |
| 🖼 [Character Sheet + Classical Illustrations](https://github.com/MatsuriMW/aigc-skills-and-agents) | Two Claude skills: prompts for three-view and expression sheets that lock a character's look; SVG explainer illustrations with an engraving texture | Usable |
| ✍️ [skills-agents-and-prompts](https://github.com/MatsuriMW/skills-agents-and-prompts) | Skills, agents and prompts: a writing pipeline, Q&A over my notes with citations, an investment research agent, image search by feel, and more | Updated regularly |

## Obsidian plugins

13 of my plugins are in the Obsidian community plugin directory; my [community profile](https://community.obsidian.md/users/matsurimw) lists all of them. The five main ones come first, then the other eight.

| Project | What it does | Status |
|---|---|---|
| 🌀 [Nautilus Spiral](https://github.com/MatsuriMW/nautilus-spiral) | Draws the events and to-dos in today's journal as a spiral. To-dos fill the gaps from "now" onward, and a capacity bar tells you whether the day fits. A main thread starts with a goal and has a progress bar you can drag; there are macOS desktop widgets. Together with Agent Deck, AI agent sessions are logged in the journal and drawn on the same spiral | In the community directory, release 2.2.0, desktop only, most complete on macOS |
| 🛰 [Agent Deck](https://github.com/MatsuriMW/obsidian-agent-deck) | Gathers AI agent sessions scattered across apps onto one deck: which agent is working, which is waiting for you and how far each has got, at a glance. To hand off work, send it from the line you're writing in your note; progress and results come back to that line. The plans you write and the work agents run end up in the same journal. [Demo video](https://matsuri.site/demo/agent-deck/) | In the community directory, release 1.2.4, desktop only |
| 🧾 [Token Receipt](https://github.com/MatsuriMW/token-receipt) | Prints a day of Claude Code, Codex and WorkBuddy token usage as a shopping receipt: tokens per model, the cost at API list prices, and how much of your subscription quota is used. The receipt feeds out of a thermal printer, or lies on a wooden table or pinned to a corkboard, and can be saved as an image or an animated SVG | In the community directory, release 1.3.1, desktop only |
| 💬 [Telegram Companion](https://github.com/MatsuriMW/telegram-companion) | Send a line from your phone and it lands in today's journal. When you want to talk, it reads your past week of journals before it answers, and afterwards writes what it learned into a profile note about you. Pick your own model; with a local Ollama your journal never leaves your computer | In the community directory, release 1.3.0, GPL-3.0, based on Telegram Inbox |
| 🔗 [Roam Backlinks](https://github.com/MatsuriMW/roam-backlinks) | Edit backlinks block by block in place, like Logseq and Roam Research, with expandable breadcrumbs and PDF export that keeps the backlinks; a per-page view shows the distinctive words and word pairs in the backlinks | In the community directory, release 1.3.1 |
| 🧰 [Obsidian-Plugins](https://github.com/MatsuriMW/Obsidian-Plugins) | Every Obsidian plugin I use myself: the local hybrid-search "second brain", an LLM Wiki, a drafting desk, task routing and more. The README rates each one: works out of the box / needs a particular way of writing / best used as a reference | Updated regularly |

The other eight, all in the directory:

| Plugin | What it does | Version |
|---|---|---|
| 🃏 [Card Walk](https://github.com/MatsuriMW/card-walk) | Review the #card flashcards and clozes in your notes on Anki's schedule, on desktop and phone, with every sync step of each answer visible | 1.1.0 |
| ✅ [Logseq Style Tasks](https://github.com/MatsuriMW/logseq-style-tasks) | Keyword tasks for Logseq-style journals: `todos` blocks, priority shorthand, keyword cycle groups with their own hotkeys, animated icons and task sounds. A fork of TODOseq | 1.0.0 |
| 🏷 [Logseq Style Alias](https://github.com/MatsuriMW/logseq-style-alias) | Like Logseq, `[[alias]]` opens the page that has that alias, instead of staying unresolved or creating an empty page | 1.0.0 |
| 📁 [Logseq Style Fold](https://github.com/MatsuriMW/logseq-style-fold) | Remembers how each list item was folded by writing Logseq's `collapsed:: true` property into the note | 1.2.0 |
| 🌲 [Emacs Logseq Inspired Outline](https://github.com/MatsuriMW/emacs-logseq-inspired-outline) | Outliner editing inspired by Logseq and Emacs: block selection, go to the parent, create at the same level, group rows | 3.3.3 |
| 📑 [Hover Outline](https://github.com/MatsuriMW/hover-outline) | A hidden table of contents in a corner of the editor that expands on hover | 1.1.0 |
| 🗂 [Chrome Tab Groups](https://github.com/MatsuriMW/obsidian-chrome-tab-groups) | Chrome-style tab groups for Obsidian | 1.1.3 |
| 🧵 [Thread Studio](https://github.com/MatsuriMW/thread-studio) | Write X posts, threads, long posts and Articles from your Obsidian notes. A fork of NoteTweet, published with the original author's permission | 1.0.0 |

## What I'm working on

- **English lesson-prep agent** (v0.3.4): a lesson-prep agent for junior-high English teachers in Wuxi. 115 real Wuxi exam papers are split into 4,012 question groups. One lesson plan fits the next exam, the school, the student's weak spots and the teacher's habits at the same time: an outline first, then the full plan once the teacher has adjusted it, in a teacher version and a student version. Student profiles are a memory that keeps itself up to date, and after-class feedback is written separately for each parent about their own child. There are two ways in, a web page and a WeChat bot; I use it to prepare my own tutoring lessons, and it's being tried out by a small group. Next comes senior high school and other cities in Jiangsu: the senior-high papers and handouts are collected, and the exam structure and question bank for senior high come next. [Demo](https://matsuri.site/demo/english-prep/)
- **[Outline Sidebar](https://github.com/MatsuriMW/outline-sidebar)**: evidence, the acceptance gate, automatic rework and follow-up questions after a failed review, the four metrics and the Desktop layout are all live, and it's under review for Claude's official plugin directory. Over the next few weeks I'm collecting data to see how much the gate actually catches.
- **Second-brain retrieval**: the local hybrid search (vectors + BM25) in Obsidian-Plugins. I built a 48-question eval set and 16 held-out questions that are never used for tuning, then tuned the refusal threshold and chunking against the bad cases: top-1 hit rate 70% → 80%, MRR 0.809 → 0.872, and of the questions the vault has no answer to, it went from refusing none to refusing all 8. A date filter came later and took the date-bound questions from MRR 0.85 to 1.0. The [online version](https://matsuri.site/demo/second-brain/) is live and adds a generation layer: bge-m3 hybrid retrieval with reranking, answers from DeepSeek; reranking lifted the top-1 hit rate from 71% to 85%. On 44 answerable questions, faithfulness is 99% and citation accuracy 100%, and all 15 questions it should refuse are refused.
- **[Public-opinion analysis workflow](https://github.com/MatsuriMW/xhs-yuqing)**: the first version runs on n8n. On a schedule it calls a Xiaohongshu MCP to fetch notes and comments about a brand; DeepSeek codes each one (is it really about this brand, sentiment, tone, red lines, mobilization level, what it's being compared with); code computes the metrics, a model writes the assessment, and code rules plus a second model grade it. After the automatic evaluation there's a human review, and misjudgments it finds are written back into the config and coding rules so the next run picks them up. [Demo](https://matsuri.site/demo/xhs-yuqing/): the 24 hours after the Tesla Roadster launch, with the assessment before and after human review. It has since moved to LangGraph (`langgraph/` in the repo): the same coding, metric and rule code, choosing Xiaohongshu, Bilibili or Zhihu as the main platform from the brand's audience profile, deciding first whether it's an incident or an ordinary day, reworking automatically when a rule fails, and stopping for human review before the report goes out. [Demo](https://matsuri.site/demo/yuqing-langgraph/): Tesla on Bilibili + Zhihu.

<p align="center">
  <a href="https://matsuri.site/demo/xhs-yuqing/"><img src="assets/xhs-yuqing-demo.jpg" width="420" alt="Public-opinion analysis demo: the 24 hours after the Tesla Roadster launch, the machine's first assessment next to the human-reviewed one"></a>
</p>
