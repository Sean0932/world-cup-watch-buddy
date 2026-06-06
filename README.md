# 世界杯观赛搭子.skill / World Cup Watch Buddy.skill

> 测测你是哪种世界杯球迷，顺手安排今晚看球。  
> Find out what kind of World Cup fan you are, then get a simple watch plan for tonight.

![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-blue)
![Runtime](https://img.shields.io/badge/runtime-Claude%20Code%20%7C%20Codex%20%7C%20OpenClaw-green)
![License](https://img.shields.io/badge/license-Apache--2.0-lightgrey)

世界杯观赛搭子是一个轻量对话型 Agent Skill：

```text
一句话触发 -> 问 5 个问题 -> 生成球迷人格 -> 给观赛建议 -> 生成小红书发布素材
```

World Cup Watch Buddy is a lightweight conversational Agent Skill:

```text
Trigger with one sentence -> ask 5 questions -> score fan persona -> suggest what to watch -> generate Xiaohongshu-ready copy
```

## Read This First

- [中文完整说明](./README.zh-CN.md)
- [Full English README](./README.en.md)
- [Skill entry](./SKILL.md)

## Quick Install

Ask your agent:

```text
帮我安装这个 skill：https://github.com/Sean0932/world-cup-watch-buddy
```

Or:

```bash
npx skills add Sean0932/world-cup-watch-buddy
```

Manual Codex install:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Sean0932/world-cup-watch-buddy.git \
  ~/.codex/skills/world-cup-watch-buddy
```

Restart your agent after installation.

## Quick Demo

```text
搭子 ❯ 来，先测测你是哪种世界杯球迷。你可以直接回复：
       1B, 2D, 阿根廷, 4B, 5A

用户 ❯ 气氛组；可以熬夜；阿根廷；兴趣哦；错过名场面

搭子 ❯ 你的球迷人格：朋友圈气氛组
       发疯指数：92%
       今晚熬不熬：可以熬，但只熬有社交价值和名场面概率的比赛。
       发圈文案：球我可以看不懂，但阿根廷的气氛我必须到位。
```

## Local Test

```bash
python3 scripts/score_persona.py \
  "气氛组 可以熬夜 阿根廷 兴趣 错过名场面" \
      --json
```

## Repository Structure

```text
world-cup-watch-buddy/
  SKILL.md
  references/
    personas.md
    watch-plan-rules.md
    xhs-copy-style.md
  scripts/
    score_persona.py
  README.zh-CN.md
  README.en.md
```

## License

Apache-2.0. See [LICENSE](./LICENSE).
