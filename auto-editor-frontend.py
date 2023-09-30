import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog
import subprocess

def drop(event):
    file_path = event.data.strip("{}")
    file_path_var.set(file_path)
    update_command_line_display()

def update_command_line_display():
    video_file_path = file_path_var.get()
    margin_value = str(margin_scale.get() / 10)
    threshold_value = str(threshold_scale.get())
    export_value = export_option_var.get()
    cmd = f'auto-editor "{video_file_path}" --margin {margin_value}sec --edit audio:threshold={threshold_value}% --export {export_value}'
    command_line_display.delete(1.0, tk.END)
    command_line_display.insert(tk.END, cmd)

def run_auto_editor():
    video_file_path = file_path_var.get()
    margin_value = str(margin_scale.get() / 10)
    threshold_value = str(threshold_scale.get())
    export_value = export_option_var.get()
    cmd = [
        "cmd.exe", "/k",
        "auto-editor", video_file_path,
        "--margin", f"{margin_value}sec",
        "--edit", f"audio:threshold={threshold_value}%",
        "--export", export_value
    ]
    subprocess.Popen(cmd)

root = TkinterDnD.Tk()
root.title("auto-editor GUI")

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

file_path_var = tk.StringVar()
file_path_var.trace("w", lambda *args: update_command_line_display())
file_path_label = tk.Label(root, text="動画ファイルへのパス:")
file_path_label.pack(pady=10)
file_path_entry = tk.Entry(root, textvariable=file_path_var, width=50)
file_path_entry.drop_target_register(DND_FILES)
file_path_entry.dnd_bind('<<Drop>>', drop)
file_path_entry.pack(pady=5)

def choose_file():
    file_path = filedialog.askopenfilename()
    file_path_var.set(file_path)

file_path_btn = tk.Button(root, text="ファイルを選択", command=choose_file)
file_path_btn.pack(pady=5)

controls_frame = tk.Frame(root)
controls_frame.pack(pady=20)

margin_label = tk.Label(controls_frame, text="Margin (sec x 0.1):")
margin_label.grid(row=0, column=0, padx=(10, 5), sticky=tk.E + tk.N + tk.S)
margin_scale = tk.Scale(controls_frame, from_=1, to=50, orient=tk.HORIZONTAL, command=lambda *args: update_command_line_display())
margin_scale.set(2)
margin_scale.grid(row=0, column=1, padx=(5, 10), sticky=tk.W + tk.N + tk.S)

threshold_label = tk.Label(controls_frame, text="Audio Threshold (%):")
threshold_label.grid(row=1, column=0, padx=(10, 5), sticky=tk.E + tk.N + tk.S)
threshold_scale = tk.Scale(controls_frame, from_=1, to=100, orient=tk.HORIZONTAL, command=lambda *args: update_command_line_display())
threshold_scale.set(3)
threshold_scale.grid(row=1, column=1, padx=(5, 10), sticky=tk.W + tk.N + tk.S)

# --export のラベルと選択肢
export_label = tk.Label(root, text="出力フォーマット:")
export_label.pack(pady=(10,0))

export_option_var = tk.StringVar(value="resolve")
export_option_var.trace("w", lambda *args: update_command_line_display())
export_options = ["resolve", "premiere", "final-cut-pro", "shotcut"]
export_option_menu = tk.OptionMenu(root, export_option_var, *export_options)
export_option_menu.pack(pady=(0,10))

run_btn = tk.Button(root, text="auto-editorを実行", command=run_auto_editor)
run_btn.pack(pady=20)

command_line_display = tk.Text(root, height=3, width=100)
command_line_display.pack(pady=10, padx=10, side=tk.LEFT, fill=tk.BOTH)
scrollbar = tk.Scrollbar(root, command=command_line_display.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
command_line_display.config(yscrollcommand=scrollbar.set)

root.geometry("600x600")
root.resizable(False, False)

root.mainloop()
