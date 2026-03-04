"""
Python pathlib入門：初心者が躓くポイントとos.pathからの脱却
- Idea-001
"""

import os
from pathlib import Path

# Python公式ドキュメント（pathlib）: https://docs.python.org/ja/3/library/pathlib.html


def dummy_legacy_function(file_path_str):
    """パスオブジェクトを受け取らず、文字列型のみをサポートする古い関数のダミー"""
    if not isinstance(file_path_str, str):
        raise TypeError("path strings must be str, not Path")
    print(f"[Legacy API] Processing file: {file_path_str}")


def main():
    print("=== 1. 基本編：パスの作成と文字列結合（os.path）からの脱却 ===")

    # 従来のやり方（os.path.join）
    base_dir_str = "/usr/local"
    sub_dir_str = "bin"
    file_name_str = "script.py"
    legacy_path = os.path.join(base_dir_str, sub_dir_str, file_name_str)
    print(f"os.path.join: {legacy_path}")

    # 初心者がよくやる文字列結合（バグの元: スラッシュの有無で事故が起きやすい）
    bad_path = base_dir_str + "/" + sub_dir_str + "/" + file_name_str
    print(f"String concatenation: {bad_path}")

    # 新しいやり方（pathlibの `/` 演算子による直感的なパス結合）
    base_dir = Path("/usr/local")
    modern_path = base_dir / "bin" / "script.py"
    print(f"pathlib (/ operator): {modern_path}")

    print("\n=== 2. 実践編：ファイルの存在確認とエラーハンドリング ===")

    # 存在しないファイルへのパスを作成
    target_file = Path("non_existent_folder") / "secret_data.txt"

    # 事前確認パターン（.exists() を使う）
    if not target_file.exists():
        print(f"Check 1: {target_file} は存在しません。（.exists()での確認）")

    # 例外処理パターン（EAFP: 許可を求めるより許しを請うほうが容易）
    try:
        with target_file.open("r", encoding="utf-8") as f:
            f.read()
    except FileNotFoundError:
        print(f"Check 2: {target_file} が見つかりませんでした。（try-exceptでの捕捉）")

    print("\n=== 3. 応用編：古いライブラリとの互換性 ===")

    # 存在するファイルのパス（自分自身）
    current_script = Path(__file__)

    try:
        # 古いライブラリにPathオブジェクトをそのまま渡すとエラーになることがある
        dummy_legacy_function(current_script)
    except TypeError as e:
        print(f"エラー発生：{e}")

    # str() でキャストして渡す
    print("-> str() でキャストして渡すと成功します:")
    dummy_legacy_function(str(current_script))


if __name__ == "__main__":
    main()
