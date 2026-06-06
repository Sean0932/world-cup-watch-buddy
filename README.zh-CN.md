# 世界杯观赛搭子.skill

> 测测你是哪种世界杯球迷，顺手安排今晚看球。

![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-blue)
![Runtime](https://img.shields.io/badge/runtime-Claude%20Code%20%7C%20Codex%20%7C%20OpenClaw-green)
![License](https://img.shields.io/badge/license-Apache--2.0-lightgrey)

世界杯观赛搭子是一个为 REDSkill 世界杯活动设计的轻量 Agent Skill。它不是世界杯百科，也不是复杂预测工具，而是一个互动生成器：

```text
一句话触发 -> 问 5 个问题 -> 生成球迷人格 -> 给观赛建议 -> 生成小红书发布文案
```

[English](./README.en.md)

---

## 效果示例

```text
用户 ❯ 测测我是世界杯哪种球迷，顺便帮我安排今晚看球。
       颜粉；年龄大了，估计能熬到 03 点；
       卡颜值；社交；朋友间交流插不上话。

搭子 ❯ 你的球迷人格：球星颜值应援官

       发疯指数：82%
       今晚熬不熬：可以熬到 03 点，但只建议熬
       “颜值主场 + 朋友会聊”的比赛。

       观赛搭子建议：
       你不是硬核战术型球迷，你的核心需求是看得开心、
       聊得上话，最好还有能截图/发圈的球星瞬间。

       发圈文案：
       今晚不是看球，是看我的世界杯门面营业。
```

如果用户问“今晚看哪场”，Skill 不会凭记忆编赛程。它会先查 FIFA 官方或可信赛程；如果 agent 不能联网，会要求用户粘贴赛程再判断。

---

## 它能做什么

- **球迷人格测试**：用 5 个轻量问题判断用户是哪种世界杯球迷。
- **观赛搭子建议**：结合支持球队、作息和赛程，判断今晚熬不熬、看哪场、怎么看。
- **社交话术**：帮气氛组、颜粉、小白用户生成朋友间能接得上的聊球话术。
- **小红书发布素材**：生成标题、封面大字、正文草稿和活动话题。
- **实时数据兜底**：涉及今晚、今天、最新赛程、比分、晋级时，要求查询或用户提供数据，不编造。

---

## 安装

这个仓库本身就是一个 skill 目录：根目录包含 `SKILL.md`、`references/` 和 `scripts/`。

### 方式一：一行命令

打开你正在使用的 Agent，告诉它：

```text
帮我安装这个 skill：https://github.com/Sean0932/world-cup-watch-buddy
```

或者使用通用 skills 安装器：

```bash
npx skills add Sean0932/world-cup-watch-buddy
```

### 方式二：手动安装

| Runtime | 安装路径 |
|---|---|
| Claude Code | `~/.claude/skills/world-cup-watch-buddy/` |
| Codex | `~/.codex/skills/world-cup-watch-buddy/` |
| OpenClaw / 小龙虾 | `~/.openclaw/workspace/skills/world-cup-watch-buddy/` |
| 其他 Agent | 放到对应 runtime 的 `skills/` 目录 |

以 Codex 为例：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Sean0932/world-cup-watch-buddy.git \
  ~/.codex/skills/world-cup-watch-buddy
```

装好后重启 Agent，告诉它：

```text
请使用 世界杯观赛搭子 这个 skill，测测我是世界杯哪种球迷。
```

---

## 工作原理

Skill 的主流程只保留一条链路：

1. 问 5 个问题。
2. 用 `scripts/score_persona.py` 稳定计算人格和发疯指数。
3. 按 `references/personas.md` 生成结果卡。
4. 如涉及实时赛程，先查官方/可信来源或要求用户粘贴赛程。
5. 按 `references/xhs-copy-style.md` 生成发布素材。

实时数据规则很重要：

```text
今晚看哪场？
今天有什么比赛？
最新比分是多少？
谁晋级了？
```

遇到这类问题，不能靠模型记忆回答。无法确认时必须说：

```text
我现在不能确认今晚官方赛程。你把今晚赛程发我，我帮你判断哪场最值得看。
```

---

## 本地测试

可以用评分脚本快速测试人格分类：

```bash
python3 scripts/score_persona.py \
  "气氛组 可以熬夜 阿根廷 兴趣 错过名场面" \
  --json
```

示例输出：

```json
{"persona":"朋友圈气氛组","persona_key":"social","madness_index":92}
```

---

## 诚实边界

- 不做世界杯百科；资料型陪看 Skill 已经有更适合的方向。
- 不提供赌博建议。
- 不输出确定性比分预测。
- 不编造赛程、比分、首发、伤停和晋级信息。
- 不鼓励用户无差别熬夜；用户表达睡眠顾虑时，优先给回放、集锦、只看关键时段等方案。

## License

Apache-2.0. See [LICENSE](./LICENSE).
