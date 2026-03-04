"""
Python内包表記：基礎から学ぶ実践例10本ノック
- Idea-002
"""

from pathlib import Path


def main():
    print("=== 1. 基礎編：リスト、辞書、集合の内包表記の基本構文 ===")
    
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


    print("\n=== 2. パラダイムシフト編：for.append()からの書き換え ===")
    
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


    print("\n=== 3. アンチパターン編：過度なネストと可読性 ===")
    
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


    print("\n=== 4. 実践編：よく使う10本ノック ===")
    
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
    # ※ブログの文脈としてpathlibの復習を兼ねる
    current_dir = Path(__file__).parent
    # ダミーで現在のファイル自身を抽出する例
    knock_10 = [p.name for p in current_dir.glob("*.py")]
    print(f"Knock 10 (Pathlib .py files): {knock_10}")
    # => Knock 10 (Pathlib .py files): ['list_comprehension.py']

if __name__ == "__main__":
    main()
