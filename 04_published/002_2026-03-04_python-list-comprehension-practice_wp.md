---
id: "002"
title: "Python内包表記：基礎から学ぶ実践例10本ノック"
slug: "python-list-comprehension-practice"
draft_date: "2026-03-04"
published_date: "2026-03-04"
status: "published"
category: "intermediate"
tags: ["python-list", "内包表記", "for文", "リファクタリング", "実践問題"]
---

# Python内包表記：基礎から学ぶ実践例10本ノック

<div class='stone-balloon'>AG先生、最近他人のPythonコードを読むと、リストの括弧 `[]` の中に長い数式や `for` とか `if` がぎっしり詰まった暗号みたいな行をよく見るんです。あれ、何ですか？</div>

<div class='ag-balloon'>ストーンさん、それは「内包表記（Comprehension）」ですね！ Pythonの特徴的な文法の一つで、リストや辞書をたった1行でスッキリ作れる魔法の構文なんです。</div>

<div class='stone-balloon'>ええっ、1行で！？ 僕はいつも空のリストを作ってから `for` で回して `append()` してるんですけど……。</div>

<div class='ag-balloon'>それでも間違いではありませんよ。でも、内包表記をマスターすれば、コードの行数が減ってバグも減り、さらに実行速度まで速くなることが多いんです。今日はその暗号を解読して、実戦で使えるように「10本ノック」に挑戦してみましょう！</div>

<figure class='wp-block-image'><img src='/images/002_python-list-comprehension-practice_01.png' alt='複雑なfor文からシンプルな内包表記へ'/></figure>

## 1. 基礎編：リスト、辞書、集合の内包表記の基本構文

<div class='ag-balloon'>内包表記の基本のカタチは `[式 for 変数 in イテラブル]` です。実はリストだけでなく、カッコの形を変えれば辞書（`{}`）や集合（`{}`）も作れるんですよ。</div>

```python
# === 1. 基礎編：リスト、辞書、集合の内包表記の基本構文 ===

# リスト内包表記の基本（0〜4の2乗）
squares_list = [i * i for i in range(5)]
print(f"List Comprehension: {squares_list}")
# => List Comprehension: [0, 1, 4, 9, 16]

# 辞書内包表記の基本（名前をキー、文字数を値に）
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(f"Dict Comprehension: {name_lengths}")
# => Dict Comprehension: {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# 集合内包表記の基本（10までの数字を3で割った余り、重複を許さない）
remainders_set = {x % 3 for x in range(10)}
print(f"Set Comprehension: {remainders_set}")
# => Set Comprehension: {0, 1, 2}
```

<div class='ag-balloon'>リストなら `[]`、辞書なら `{キー: 値 for ...}`、集合なら `{式 for ...}` と書くだけなんです。</div>
<div class='stone-balloon'>わぁ、ホントだ！カッコを変えるだけで辞書まで作れちゃうんですね！</div>

## 2. パラダイムシフト編：for.append()からの書き換え

<div class='stone-balloon'>でも先生、やっぱり `for` と `if` が混ざるとどう読んで良いか分からなくなります。</div>

<div class='ag-balloon'>じゃあ、見慣れた `append()` のコードと見比べて、「どこがどう移動したか」を下から上へパズルみたいに当てはめてみましょう。</div>

```python
# === 2. パラダイムシフト編：for.append()からの書き換え ===

# 従来の for と append() を使ったコード
evens_legacy = []
for num in range(10):
    if num % 2 == 0:
        evens_legacy.append(num)
print(f"Legacy for-loop: {evens_legacy}")
# => Legacy for-loop: [0, 2, 4, 6, 8]

# 内包表記に書き換えたコード
evens_modern = [num for num in range(10) if num % 2 == 0]
print(f"Modern Comprehension: {evens_modern}")
# => Modern Comprehension: [0, 2, 4, 6, 8]
```

<div class='ag-balloon'>まず一番左の `num` が「最終的に追加したい式（`append()`の中身）」です。その次に「ループ（`for`）」、最後に「条件（`if`）」が続きます。</div>
<div class='stone-balloon'>なるほど！「何を」「どう回して」「どんな条件で」の順番に並んでいるんですね。そうやって分解して読めば怖くないかも。</div>

## 3. アンチパターン編：過度なネストと可読性

<div class='stone-balloon'>面白くなってきました！ じゃあ、for文を3重くらいネストさせて、if文もたくさん繋げて、超絶アクロバティックな1行コードにしちゃってもいいんですか！？</div>

<div class='ag-balloon'>ストーンさん、落ち着いて！（笑） それが一番やってはいけない「アンチパターン」です。</div>

```python
# === 3. アンチパターン編：過度なネストと可読性 ===

# 悪い例：可読性の低い多重ループ（1行に詰め込みすぎ）
# bad_pattern = [x * y for x in range(1, 4) for y in range(1, 4) if x != y if x % 2 == 0]

# 良い例：適切な改行と適度な分割を用いたコード
good_pattern = [
    x * y
    for x in range(1, 4)
    for y in range(1, 4)
    if x != y and x % 2 == 0
]
print(f"Readable Nested Comprehension: {good_pattern}")
# => Readable Nested Comprehension: [2, 6]
```

<div class='ag-balloon'>何でもかんでも1行に詰め込めば良いというものではありません。`for` や `if` が複数重なるような複雑な処理は、可読性が著しく低下します。無理に1行にせず、カッコ内で適切に改行を入れてあげるのが「良いコード」の秘訣ですよ。</div>

<figure class='wp-block-image'><img src='/images/002_python-list-comprehension-practice_02.png' alt='複雑なネストを適切に整理するAG先生'/></figure>

## 4. 実践編：よく使う10本ノック

<div class='stone-balloon'>分かりました！ 可読性を意識しながら、実戦でどう使うのかもっと教えてください。</div>

<div class='ag-balloon'>もちろんです。実務や競技プログラミングなどですぐに使える具体的なパターンを10個連続でお見せしますよ！</div>

```python
# === 4. 実践編：よく使う10本ノック ===

# ノック1: 数値リストから偶数だけを抽出（フィルタリング）
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
knock_1 = [n for n in numbers if n % 2 == 0]
print(f"Knock 1 (Filter evens): {knock_1}")
# => Knock 1 (Filter evens): [2, 4, 6, 8, 10]

# ノック2: 文字列リストから特定の文字を含むものを抽出
words = ["apple", "banana", "cherry", "date"]
knock_2 = [w for w in words if "a" in w]
print(f"Knock 2 (Contains 'a'): {knock_2}")
# => Knock 2 (Contains 'a'): ['apple', 'banana', 'date']

# ノック3: 全要素の型変換（strからintへ）
str_nums = ["10", "20", "30"]
knock_3 = [int(s) for s in str_nums]
print(f"Knock 3 (Str to Int): {knock_3}")
# => Knock 3 (Str to Int): [10, 20, 30]

# ノック4: リスト内の文字列をすべて大文字に変換
knock_4 = [w.upper() for w in words]
print(f"Knock 4 (To Uppercase): {knock_4}")
# => Knock 4 (To Uppercase): ['APPLE', 'BANANA', 'CHERRY', 'DATE']

# ノック5: 2次元リスト（行列）の平坦化（フラット化）
matrix = [[1, 2], [3, 4], [5, 6]]
knock_5 = [val for row in matrix for val in row]
print(f"Knock 5 (Flatten Matrix): {knock_5}")
# => Knock 5 (Flatten Matrix): [1, 2, 3, 4, 5, 6]

# ノック6: 条件演算子（三項演算子）を組み合わせたデータ置換
knock_6 = ["Even" if n % 2 == 0 else "Odd" for n in range(1, 6)]
print(f"Knock 6 (Even/Odd replacement): {knock_6}")
# => Knock 6 (Even/Odd replacement): ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# ノック7: 辞書のキーとバリューを入れ替える（辞書内包表記）
original_dict = {"a": 1, "b": 2, "c": 3}
knock_7 = {v: k for k, v in original_dict.items()}
print(f"Knock 7 (Swap Dict Key/Value): {knock_7}")
# => Knock 7 (Swap Dict Key/Value): {1: 'a', 2: 'b', 3: 'c'}

# ノック8: 2つのリストから辞書を作成（辞書内包表記 + zip）
keys = ["id", "name", "role"]
values = [101, "Stone", "Admin"]
knock_8 = {k: v for k, v in zip(keys, values)}
print(f"Knock 8 (Zip to Dict): {knock_8}")
# => Knock 8 (Zip to Dict): {'id': 101, 'name': 'Stone', 'role': 'Admin'}

# ノック9: 文字列内の重複しない文字を抽出（集合内包表記）
text = "abracadabra"
knock_9 = {char for char in text}
print(f"Knock 9 (Unique chars in Set): {knock_9}")
# => Knock 9 (Unique chars in Set): {'c', 'b', 'r', 'd', 'a'}

# ノック10: pathlib と組み合わせた、特定拡張子（.py）のファイル名リスト作成
from pathlib import Path
current_dir = Path(__file__).parent
knock_10 = [p.name for p in current_dir.glob("*.py")]
print(f"Knock 10 (Pathlib .py files): {knock_10}")
# => Knock 10 (Pathlib .py files): ['list_comprehension.py']
```

<div class='ag-balloon'>文字列のフィルタリングから型変換、辞書のキー・バリュー入れ替えなど、内包表記はデータの変形に大活躍します。さらに、前回学んだ `pathlib` と組み合わせれば、「特定フォルダ内の `.py` ファイル名だけをリストアップする」なんてこともたった1行で書けちゃうんです！</div>
<div class='stone-balloon'>（拍手）エビのハサミでもこれならスラスラ入力できそう🦐！ 10本ノックで完全にコツを掴みました。ありがとうございます、AG先生！</div>

---

<div class='ag-recommend'>
<div class='ag-balloon'>ストーンさん、内包表記の見やすさに感動した方に、ぜひおすすめしたい一冊があるんです。</div>
<div class='stone-balloon'>わあ、なんですか！？</div>
<div class='ag-balloon'><strong>『Effective Python 第2版――Pythonプログラムを改良する90項目』</strong> です。</div>
[text](https://amzn.to/4b0V8US)
<div class='stone-balloon'>イフェクティブ……響きからして強そうですね🦐</div>
<div class='ag-balloon'>今回紹介した「内包表記は複雑にしすぎない」といったベストプラクティスが90項目にわたって詳しく解説されている名著ですよ。よりステップアップしたいストーンさんには必読の一冊です！</div>
</div>
