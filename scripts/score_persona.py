#!/usr/bin/env python3
"""Score the World Cup fan persona from five lightweight answers."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Persona:
    key: str
    name: str
    base_score: int
    summary: str


PERSONAS = {
    "miracle": Persona("miracle", "补时玄学大师", 82, "越到补时越精神，专等名场面发生。"),
    "serious": Persona("serious", "凌晨硬撑型真球迷", 76, "主队优先，全场陪跑，认真但不乱上头。"),
    "social": Persona("social", "朋友圈气氛组", 64, "看球不一定最懂，但气氛一定到位。"),
    "casual": Persona("casual", "大赛限定快乐人", 56, "四年一次加入战局，主打快乐和名场面。"),
    "star": Persona("star", "球星颜值应援官", 70, "跟着球星看世界杯，应援和截图都不能少。"),
    "tactics": Persona("tactics", "战术板上头玩家", 72, "喜欢看阵型、换人和中场博弈。"),
    "sleep": Persona("sleep", "第二天保命派", 42, "爱看球，也爱明天还能正常生活。"),
    "survival": Persona("survival", "伪装懂球求生员", 52, "先学会几句靠谱话术，应付朋友提问。"),
}


def add(scores: dict[str, int], key: str, value: int) -> None:
    scores[key] = scores.get(key, 0) + value


def score_answers(answers: list[str]) -> dict[str, object]:
    text = " ".join(answers).lower()
    scores = {key: 0 for key in PERSONAS}

    keyword_rules = [
        ("真球迷", "serious", 5),
        ("主队", "serious", 4),
        ("支持", "serious", 3),
        ("懂球", "tactics", 5),
        ("战术", "tactics", 5),
        ("朋友问", "survival", 5),
        ("看法", "survival", 3),
        ("气氛组", "social", 8),
        ("气氛", "social", 6),
        ("社交", "social", 6),
        ("发小红书", "social", 5),
        ("发圈", "social", 5),
        ("大赛限定", "casual", 5),
        ("纯快乐", "casual", 4),
        ("球星", "star", 5),
        ("颜粉", "star", 6),
        ("名场面", "miracle", 5),
        ("补时", "miracle", 5),
        ("点球", "miracle", 4),
        ("第二天", "sleep", 6),
        ("废掉", "sleep", 6),
        ("不能熬", "sleep", 6),
        ("不熬", "sleep", 5),
    ]

    for keyword, key, value in keyword_rules:
        if keyword.lower() in text:
            add(scores, key, value)

    if any(hour in text for hour in ["23", "十一", "11点", "12点", "0点", "零点"]):
        add(scores, "sleep", 4)
    if any(hour in text for hour in ["1点", "一点", "2点", "两点"]):
        add(scores, "casual", 2)
        add(scores, "sleep", 2)
    if any(hour in text for hour in ["3点", "三点", "通宵", "天亮"]):
        add(scores, "miracle", 3)
        add(scores, "serious", 3)

    winner_key = max(scores, key=lambda key: (scores[key], PERSONAS[key].base_score))
    if scores["sleep"] >= 12 and scores[winner_key] - scores["sleep"] <= 5:
        winner_key = "sleep"
    persona = PERSONAS[winner_key]
    madness = max(20, min(98, persona.base_score + scores[winner_key] * 2))

    return {
        "persona": persona.name,
        "persona_key": persona.key,
        "madness_index": madness,
        "summary": persona.summary,
        "scores": scores,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Score a World Cup fan persona.")
    parser.add_argument("answers", nargs="*", help="Five user answers, or one combined answer string.")
    parser.add_argument("--json", action="store_true", help="Print compact JSON only.")
    args = parser.parse_args()

    result = score_answers(args.answers)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
        return

    print(f"你的球迷人格：{result['persona']}")
    print(f"发疯指数：{result['madness_index']}%")
    print(result["summary"])


if __name__ == "__main__":
    main()
