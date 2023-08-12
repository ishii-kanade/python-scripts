import tkinter as tk
from tkinter import filedialog


def add_spaces_and_newline(text):
    return text.replace("。", "。  \n")


def process_markdown_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    modified_content = add_spaces_and_newline(content)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(modified_content)

    result_label.config(text="変換が完了しました！")


def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
    if filepath:
        process_markdown_file(filepath)


app = tk.Tk()
app.title("Markdown変換ツール")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

open_btn = tk.Button(frame, text="マークダウンファイルを選択", command=open_file)
open_btn.pack(pady=20)

result_label = tk.Label(frame, text="")
result_label.pack(pady=20)

app.mainloop()
