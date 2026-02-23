# Skill: Blog SEO & Taxonomy Manager
記事の内容に基づき、最適なカテゴリー、タグ、URLスラッグを自動設定する。

## Capabilities
1. **Category Mapping**: `taxonomy_master.json` を参照し、記事の内容に最も近いカテゴリーを選択する。
2. **Tag Selection**: 既存タグの再利用を優先しつつ、必要に応じて新規タグを2つまで提案する。
3. **Smart Slug Generation**: 記事のメインテーマ（英語）を抽出し、SEOに強い簡潔なスラッグを生成する。

## Instruction Context
- スラッグ例: `pathlib-file-operation-tips`
- カテゴリー例: 内容がA*なら「アルゴリズム詳解」を選択。