# AI PowerPoint Generator

AIとの対話を通じて、設計→デザイン→生成のフローでPowerPoint資料を作成するシステムです。

## セットアップ

```bash
uv sync
```

## 使い方

### 1. AIとの対話で資料を設計する

AIに資料の目的・構成・デザインを相談し、決定事項はADRとして `docs/adr/` に記録されます。

### 2. JSON仕様を作成する

対話の結果を以下の形式のJSONにまとめます:

```json
{
  "output": "output/my-presentation.pptx",
  "design": {
    "font_name": "Meiryo",
    "title_size": 32,
    "body_size": 18
  },
  "slides": [
    {"layout": "title", "title": "発表タイトル", "body": "サブタイトル"},
    {"layout": "content", "title": "概要", "body": ["ポイント1", "ポイント2"]},
    {"layout": "section", "title": "セクション区切り"},
    {"layout": "content", "title": "詳細", "body": "本文テキスト", "notes": "スピーカーノート"}
  ]
}
```

### 3. PPTXを生成する

```python
from src.workflow import generate_from_spec
generate_from_spec("spec.json")
```

## プロジェクト構造

```
├── docs/adr/          # 対話の決定記録(ADR)
├── src/
│   ├── generator.py   # PPTX生成コアモジュール
│   └── workflow.py    # 対話フロー管理
├── output/            # 生成されたPPTXファイル
└── pyproject.toml
```

## スライドレイアウト

| layout | 用途 |
|--------|------|
| `title` | タイトルスライド |
| `content` | 通常コンテンツ |
| `section` | セクション区切り |
| `blank` | 白紙 |

## 対話フロー

1. **設計フェーズ**: 資料の目的、対象者、構成を決定
2. **デザインフェーズ**: フォント、配色、レイアウト方針を決定
3. **生成フェーズ**: JSON仕様を確定し、PPTXを出力

各フェーズの決定は `docs/adr/` にADR形式で記録されます。
