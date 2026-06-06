# World Cup Watch Buddy.skill

> Find out what kind of World Cup fan you are, then get a simple watch plan for tonight.

![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-blue)
![Runtime](https://img.shields.io/badge/runtime-Claude%20Code%20%7C%20Codex%20%7C%20OpenClaw-green)
![License](https://img.shields.io/badge/license-Apache--2.0-lightgrey)

World Cup Watch Buddy is a lightweight conversational Agent Skill for REDSkill-style World Cup content.

It is not an encyclopedia and not a betting predictor. It is an interactive generator:

```text
Trigger with one sentence -> ask 5 questions -> score fan persona -> suggest what to watch -> generate Xiaohongshu-ready copy
```

[中文说明](./README.zh-CN.md)

---

## Who It Is For

- Users who want to join the REDSkill World Cup activity without building a complex tool.
- Casual fans who care about vibes, players, social moments, and highlights.
- People who want to know whether tonight is worth staying up for.
- Creators who need a Xiaohongshu title, cover text, post draft, and hashtags.
- Agents or developers testing whether a GitHub-hosted Skill can be installed and used correctly.

---

## One-Sentence Experience

The user says:

```text
Test what kind of World Cup fan I am, and help me plan tonight.
```

The skill asks 5 questions:

```text
1. Are you a serious fan, vibe fan, tournament-only fan, or player visual fan?
2. What is the latest time you can stay up?
3. Do you support any team or player?
4. Are you watching for tactics, social chat, Xiaohongshu content, or pure fun?
5. Are you more afraid of missing a big moment, being exhausted tomorrow, or not knowing what to say with friends?
```

Then it outputs a result card:

```text
Your fan persona: Social Vibe Fan

Madness index: 92%
Should you stay up tonight: Yes, but only for matches with social value and high big-moment potential.
Watch buddy advice: Prioritize Argentina matches. For other matches, only stay up for heavyweight clashes, knockouts, stoppage-time drama, or penalty shootouts.
Social copy: I may not understand every tactic, but I am absolutely here for Argentina vibes.
Xiaohongshu title: I asked a Skill to test my World Cup fan persona, and it called me a Social Vibe Fan
Cover text: My Fan Persona Is Out
Hashtags: #REDSkill #对世界杯动手了 #世界杯聊个球
```

---

## Full Examples

### Example 1: Social Vibe Fan

```text
User ❯ Vibe fan; I can stay up; Argentina; just interested; afraid of missing big moments.

Buddy ❯ Your fan persona: Social Vibe Fan

        Madness index: 92%

        Should you stay up tonight:
        Yes, but only for matches with social value and high big-moment potential.

        Watch buddy advice:
        You are not just randomly following the crowd. You support Argentina
        and you care about big moments, so your best strategy is:
        watch Argentina matches first; for non-Argentina matches, only stay up
        for heavyweight clashes, knockout games, stoppage-time drama, or penalties.

        Social copy:
        I may not understand every tactic, but I am absolutely here for Argentina vibes.
```

### Example 2: Star Visual Supporter

```text
User ❯ Mostly here for good-looking players; can stay up until 3 AM;
       social chat; I often cannot join football conversations.

Buddy ❯ Your fan persona: Star Visual Supporter

        Madness index: 82%

        Should you stay up tonight:
        You can stay up until 3 AM, but only for a high-discussion match
        with players you actually care about.

        Watch buddy advice:
        You do not need to pretend to be a tactics expert. Your core need is:
        enjoy the match, follow player moments, and have something easy to say
        when friends start talking.

        Conversation line:
        I am not pretending to be a tactics expert. I am mostly watching player form
        and match energy, but the rhythm of this match does feel tight.

        Social copy:
        Tonight is not just football. It is World Cup main-character time.
```

### Example 3: Sleep-Safe Fan

```text
User ❯ Vibe fan; must sleep before 1 AM; no fixed team;
       want to post on Xiaohongshu; afraid of being useless tomorrow.

Buddy ❯ Your fan persona: Sleep-Safe Fan

        Madness index: 70%

        Should you stay up tonight:
        Do not force it. You are better off watching highlights tomorrow morning.

        Watch buddy advice:
        If it is not your team, a knockout match, the final, or a match everyone
        will talk about, do not turn an ordinary fixture into a personal survival test.

        Social copy:
        I love football, but I also love being functional tomorrow.
```

---

## What It Does

| Capability | Output |
|---|---|
| Fan persona test | One of 8 personas such as Social Vibe Fan, Star Visual Supporter, Stoppage-Time Mystic, Sleep-Safe Fan |
| Madness index | A lightweight 0-100% entertainment score |
| Watch plan | Stay up or not, full match or highlights, what type of match is worth watching |
| Conversation lines | Safe football chat lines for casual fans |
| Xiaohongshu copy | Title, cover text, post draft, and event hashtags |
| Real-time data guardrail | Requires verified schedule, score, advancement, lineup, or injury data |

---

## Why It Is Not a World Cup Encyclopedia

This skill is designed for fast interaction and shareable output.

It intentionally does not provide:

- A full World Cup knowledge base.
- Real-time score tracking.
- Betting, odds, or wagering advice.
- Complex winner-probability models.

It does one thing:

```text
Help the user identify their fan persona and decide how to watch tonight comfortably.
```

---

## Installation

This repository is itself a Skill directory. The root contains:

```text
SKILL.md
references/
scripts/
```

### Option 1: Ask Your Agent to Install It

In Codex, Claude Code, OpenClaw, or another compatible agent, say:

```text
Install this skill: https://github.com/Sean0932/world-cup-watch-buddy
```

Restart the agent after installation.

### Option 2: Use a Skills Installer

```bash
npx skills add Sean0932/world-cup-watch-buddy
```

If your installer supports runtime flags, add the relevant one, such as `-a codex`, `-a claude-code`, or `-a openclaw`.

### Option 3: Manual Install

| Runtime | Recommended path |
|---|---|
| Codex | `~/.codex/skills/world-cup-watch-buddy/` |
| Claude Code | `~/.claude/skills/world-cup-watch-buddy/` |
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

## Quick Test Prompts

After installing, try:

```text
Use World Cup Watch Buddy to test what kind of World Cup fan I am and help me plan tonight.
```

```text
I am a vibe fan, I can stay up, I support Argentina, I care about social chat, and I do not want to miss big moments. Generate my result card and Xiaohongshu copy.
```

```text
I mostly watch for player visuals and I can stay up until 3 AM, but I cannot join football conversations. Test my persona and give me a few safe conversation lines.
```

```text
I do not want to stay up, but I still want to join the World Cup conversation. Test my persona and give me a no-late-night plan.
```

---

## Real-Time Fixture Rule

This skill does not embed live schedules and must not invent fixtures from model memory.

For requests like:

```text
What should I watch tonight?
What matches are on today?
What is the latest score?
Who advanced?
Who is starting?
Who is injured?
```

The agent must verify current information using:

- FIFA official schedule.
- A schedule pasted by the user.
- A trusted sports platform.

If verification is unavailable, the agent must say:

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
{
  "persona": "朋友圈气氛组",
  "persona_key": "social",
  "madness_index": 92,
  "summary": "看球不一定最懂，但气氛一定到位。"
}
```

Another test:

```bash
python3 scripts/score_persona.py \
  "气氛组 1点前睡 没有支持球队 为了发小红书 怕第二天废掉" \
  --json
```

---

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
  README.md
  README.zh-CN.md
  README.en.md
  LICENSE
```

| File | Purpose |
|---|---|
| `SKILL.md` | Skill trigger, main workflow, and real-time data rules |
| `references/personas.md` | 8 fan persona definitions |
| `references/watch-plan-rules.md` | Watch planning, stay-up logic, and schedule fallback rules |
| `references/xhs-copy-style.md` | Xiaohongshu title, cover, post, and hashtag templates |
| `scripts/score_persona.py` | Stable persona and madness-index scoring |

---

## Boundaries

- No betting advice.
- No deterministic score predictions.
- No invented fixtures, scores, lineups, injuries, or advancement status.
- No blanket encouragement to stay up all night.
- Sleep-sensitive users should get replay, highlights, or key-moment plans.

## License

Apache-2.0. See [LICENSE](./LICENSE).
