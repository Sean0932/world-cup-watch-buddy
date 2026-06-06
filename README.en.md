# World Cup Watch Buddy.skill

> Find out what kind of World Cup fan you are, then get a simple watch plan for tonight.

![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-blue)
![Runtime](https://img.shields.io/badge/runtime-Claude%20Code%20%7C%20Codex%20%7C%20OpenClaw-green)
![License](https://img.shields.io/badge/license-Apache--2.0-lightgrey)

World Cup Watch Buddy is a lightweight conversational Agent Skill for REDSkill-style World Cup content. It is not an encyclopedia and not a betting predictor. It is an interactive generator:

```text
Trigger with one sentence -> ask 5 questions -> score fan persona -> suggest what to watch -> generate Xiaohongshu-ready copy
```

[中文说明](./README.zh-CN.md)

---

## Example

```text
User ❯ Test what kind of World Cup fan I am, and help me plan tonight.
       I am mostly here for good-looking players;
       I can stay up until around 3 AM;
       I want to join the conversation with friends.

Buddy ❯ Your fan persona: Star Visual Supporter

        Madness index: 82%
        Should you stay up tonight:
        Yes, but only for a high-discussion match with players
        you actually care about.

        Watch buddy advice:
        You do not need to pretend to be a tactics expert.
        Pick a match that your friends will talk about, watch
        the player moments, and use a few safe conversation lines.

        Social copy:
        Tonight is not just football. It is World Cup main-character time.
```

If the user asks what to watch tonight, the skill must not invent fixtures from memory. It should check FIFA or another trusted schedule source first. If the agent cannot browse, it should ask the user to paste the schedule.

---

## What It Does

- **Fan persona test**: Scores the user from 5 lightweight answers.
- **Watch plan**: Suggests whether to stay up, what type of match to prioritize, and how to watch.
- **Conversation lines**: Helps casual fans join football conversations without pretending too hard.
- **Xiaohongshu-ready copy**: Generates titles, cover text, post drafts, and event hashtags.
- **Real-time data guardrail**: Requires fresh schedule or user-provided data for current fixtures, scores, advancement, lineups, and injuries.

---

## Installation

This repository is itself a skill directory. The root contains `SKILL.md`, `references/`, and `scripts/`.

### One-line install

Ask your agent:

```text
Install this skill: https://github.com/Sean0932/world-cup-watch-buddy
```

Or use a general skills installer:

```bash
npx skills add Sean0932/world-cup-watch-buddy
```

### Manual install

| Runtime | Path |
|---|---|
| Claude Code | `~/.claude/skills/world-cup-watch-buddy/` |
| Codex | `~/.codex/skills/world-cup-watch-buddy/` |
| OpenClaw | `~/.openclaw/workspace/skills/world-cup-watch-buddy/` |
| Other agents | Put it under the runtime's `skills/` directory |

For Codex:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Sean0932/world-cup-watch-buddy.git \
  ~/.codex/skills/world-cup-watch-buddy
```

Then restart the agent and say:

```text
Use the World Cup Watch Buddy skill to test what kind of World Cup fan I am.
```

---

## How It Works

The skill keeps one simple flow:

1. Ask 5 questions.
2. Use `scripts/score_persona.py` for stable persona scoring.
3. Use `references/personas.md` to write the result card.
4. For real-time fixtures or scores, check a trusted source or ask the user to paste the schedule.
5. Use `references/xhs-copy-style.md` for Xiaohongshu-style output.

Important real-time data rule:

```text
What should I watch tonight?
What matches are on today?
What is the latest score?
Who advanced?
```

For these requests, do not rely on model memory. If the agent cannot verify the schedule, say:

```text
I cannot confirm the official schedule right now. Paste tonight's schedule and I will help you decide which match is most worth watching.
```

---

## Local Test

Run the scoring script:

```bash
python3 scripts/score_persona.py \
  "气氛组 可以熬夜 阿根廷 兴趣 错过名场面" \
  --json
```

Example:

```json
{"persona":"朋友圈气氛组","persona_key":"social","madness_index":92}
```

---

## Boundaries

- Not a World Cup encyclopedia.
- No betting advice.
- No deterministic score predictions.
- No invented fixtures, scores, lineups, injuries, or advancement status.
- No blanket encouragement to stay up all night; sleep-sensitive users get replay, highlights, or key-moment plans.

## License

Apache-2.0. See [LICENSE](./LICENSE).
