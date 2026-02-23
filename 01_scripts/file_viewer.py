import pathlib

def view_file(file_path):
    path = pathlib.Path(file_path)
    # 意図的に exists() チェックを行わずに読み込む（Issue #1 対応前）
    content = path.read_text(encoding="utf-8")
    print(content)

if __name__ == "__main__":
    view_file("non_existent_directory/some_file.txt")
