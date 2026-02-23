# Issue #1 が立った！pathlibでのファイル読み込み時の罠

記念すべき Issue #1 が立ちました！
今回は `pathlib` を使って単純にファイルの中身を読み込もうと思ったら、存在しないディレクトリの指定でクラッシュしてしまった、という事象についてです。

## 今のコードへのツッコミ

[USER]: ファイルの中身をサクッと読み込みたくて書いたんだけど、エラーが出ちゃうんだよね。
[AG]: コードを見てみましょう。あー、なるほど。`path.read_text()` をそのまま呼び出していますね。
[USER]: そうそう。シンプルでいいでしょ？
[AG]: シンプルさは素晴らしいですが、指定したファイルやディレクトリが存在しない場合の考慮（ガード処理）が抜けていますね。このままだと、存在しないパスが渡された時に無慈悲に \`FileNotFoundError\` でクラッシュしてしまいますよ。
[USER]: 確かに…。どうすればいい？
[AG]: `path.exists()` や `path.is_file()` を使って、事前に存在チェックを入れるのが定石です。Issueでもまさにそこが指摘されていますね！

---
**Category:** Python Troubleshooting
**Tags:** Python, pathlib, Issue, Error
**URL Slug:** pathlib-file-read-exists-check
