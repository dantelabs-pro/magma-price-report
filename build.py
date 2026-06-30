#!/usr/bin/env python3
"""MAGMA 가격 리포트 빌더.

data/*.json 의 세그먼트별 가격 데이터를 읽어 templates/report.html.tmpl 에
끼워 넣고, 배포용 정적 페이지(_site/index.html)를 만든다.

의존성 없음(파이썬 표준 라이브러리만). 그래서 누구 컴퓨터에서도, GitHub
Actions 에서도 pip 설치 없이 그대로 돈다.
"""
import json
import pathlib
import string

ROOT = pathlib.Path(__file__).parent
DATA = ROOT / "data"
OUT = ROOT / "_site"

SEGMENTS = ["budget", "mid", "premium"]  # 저가 / 중가 / 프리미엄
LABELS = {"budget": "저가", "mid": "중가", "premium": "프리미엄"}


def load_segment(name: str) -> list[dict]:
    """data/<segment>.json 을 읽는다. 파일이 없으면 빈 목록(아직 안 채운 세그먼트)."""
    path = DATA / f"{name}.json"
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def render_rows() -> str:
    rows = []
    for seg in SEGMENTS:
        for item in load_segment(seg):
            rows.append(
                f"<tr><td>{LABELS[seg]}</td><td>{item['name']}</td>"
                f"<td class='price'>{item['price']:,}원</td></tr>"
            )
    if not rows:
        return "<tr><td colspan='3'>아직 데이터가 없습니다.</td></tr>"
    return "\n".join(rows)


def main() -> None:
    template = string.Template((ROOT / "templates" / "report.html.tmpl").read_text(encoding="utf-8"))
    html = template.substitute(rows=render_rows())
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(html, encoding="utf-8")
    print(f"[build] _site/index.html 생성 완료 ({len(html)} bytes)")


if __name__ == "__main__":
    main()
