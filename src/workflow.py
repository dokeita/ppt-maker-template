"""対話フロー管理 - 設計→デザイン→生成の各フェーズを管理する"""

import json
from datetime import datetime
from pathlib import Path
from src.generator import create_presentation

DOCS_DIR = Path("docs/adr")


def save_adr(number: int, title: str, phase: str, context: str, decision: str, reason: str, result: str = "") -> Path:
    """対話の決定をADRとして保存する。"""
    content = f"""# ADR-{number:03d}: {title}

## ステータス
承認

## フェーズ
{phase}

## コンテキスト
{context}

## 決定
{decision}

## 理由
{reason}

## 結果
{result}

---
記録日時: {datetime.now().isoformat()}
"""
    path = DOCS_DIR / f"{number:03d}-{title.replace(' ', '-')}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def get_next_adr_number() -> int:
    """次のADR番号を取得する。"""
    existing = list(DOCS_DIR.glob("[0-9][0-9][0-9]-*.md"))
    if not existing:
        return 1
    numbers = [int(p.stem.split("-")[0]) for p in existing]
    return max(numbers) + 1


def generate_from_spec(spec_path: str) -> str:
    """JSON仕様ファイルからPPTXを生成する。

    spec_pathのJSONフォーマット:
    {
        "output": "output/presentation.pptx",
        "design": {"font_name": "Meiryo", "title_size": 32, "body_size": 18},
        "slides": [
            {"layout": "title", "title": "...", "body": "..."},
            {"layout": "content", "title": "...", "body": ["item1", "item2"]}
        ]
    }
    """
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    return create_presentation(
        slides_data=spec["slides"],
        output_path=spec.get("output", "output/presentation.pptx"),
        design=spec.get("design"),
    )
