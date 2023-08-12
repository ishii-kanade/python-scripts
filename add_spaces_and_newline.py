def add_spaces_and_newline(text):
    return text.replace('。', '。  \n')

def process_markdown_file(filepath):
    # ファイルの内容を読み込む
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # 「。」の後に半角スペース２つと改行を挿入する処理を実行
    modified_content = add_spaces_and_newline(content)

    # 結果を同じファイルに上書き保存
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(modified_content)

# 使用例
filepath = 'path_to_your_markdown_file.md'
process_markdown_file(filepath)
