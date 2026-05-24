# AI PowerPoint Generator

python-pptxを使い、AIとの対話で設計→デザイン→生成のフローでPowerPoint資料を作成するシステム。

## 対話フロー
1. **設計フェーズ**: 資料の目的、対象者、構成を決定
2. **デザインフェーズ**: フォント、配色、レイアウト方針を決定
3. **生成フェーズ**: JSON仕様を確定し、PPTXを出力

## ADR記録ルール
- 各フェーズでの決定は `docs/adr/` にADR形式で記録する
- ファイル名: `{番号:03d}-{タイトル}.md`
- `docs/adr/000-template.md` のテンプレートに従う
- `src/workflow.py` の `save_adr()` を使って記録する

## コード規約
- Python 3.11+
- パッケージ管理: uv (`uv sync` でセットアップ)
- スライド仕様はJSON形式で定義する

## スライドJSON仕様
```json
{
  "output": "output/ファイル名.pptx",
  "design": {"font_name": "Meiryo", "title_size": 32, "body_size": 18},
  "slides": [
    {"layout": "title|content|section|blank", "title": "...", "body": "...|[...]", "notes": "..."}
  ]
}
```

## 生成
`src/workflow.py` の `generate_from_spec(spec_path)` でJSON仕様からPPTXを生成する。
