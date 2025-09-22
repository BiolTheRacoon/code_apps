import os
import subprocess
import shutil
import json
import csv
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

# Stage 3: Modular functions, full CSV/JSON/TXT support, editor switching

BASE_PATH = Path.home() / "PycharmProjects" / "test_file" / "texts"
BASE_PATH.mkdir(parents=True, exist_ok=True)

CONFIG_FILE = Path.home() / ".text_opener_config.json"

def load_preferred_editor():
    if CONFIG_FILE.exists():
        with CONFIG_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
            editor = data.get("preferred_editor")
            if editor and shutil.which(editor):
                return editor
    return pick_editor()

def pick_editor():
    editors = ["code", "mousepad", "nano"]
    available = [e for e in editors if shutil.which(e)]
    for i, e in enumerate(available, start=1):
        print(f"[{i}] {e}")
    choice = input("Enter number > ").strip()
    try:
        idx = int(choice) - 1
        editor = available[idx]
    except (ValueError, IndexError):
        editor = available[0]
    with CONFIG_FILE.open("w", encoding="utf-8") as f:
        json.dump({"preferred_editor": editor}, f)
    return editor

def open_with_editor(filepath, editor):
    try:
        subprocess.Popen([editor, str(filepath)])
        print(f"Opening '{filepath}' with {editor}...")
    except Exception as e:
        print(f"Error opening file with {editor}: {e}")

def create_file(filename, content):
    file_path = BASE_PATH / filename
    with file_path.open("w", encoding="utf-8") as f:
        f.write(content)
    print(f"File '{filename}' created successfully!")

def read_file(file_path):
    ext = file_path.suffix.lower()
    if ext == ".json":
        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            print(json.dumps(data, indent=4))
    elif ext == ".csv":
        with file_path.open("r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    else:
        with file_path.open("r", encoding="utf-8") as f:
            print(f.read())

def delete_file(filename):
    file_path = BASE_PATH / filename
    if file_path.exists():
        confirm = input(f"Delete '{filename}'? [y/N] > ").strip().lower()
        if confirm == "y":
            file_path.unlink()
            print(f"File '{filename}' deleted.")
        else:
            print("Delete canceled.")
    else:
        print("File not found.")

preferred_editor = load_preferred_editor()

while True:
    action = input("Action: [open], [create], [delete], [read], [change editor], [quit] > ").strip().lower()
    if action == "open":
        root = tk.Tk()
        root.withdraw()
        filepath = filedialog.askopenfilename(initialdir=BASE_PATH, title="Select a file")
        root.destroy()
        if filepath:
            open_with_editor(Path(filepath), preferred_editor)
    elif action == "create":
        filename = input("Enter filename: ").strip()
        content = input("Enter file content: ")
        create_file(filename, content)
    elif action == "delete":
        filename = input("Enter filename: ").strip()
        delete_file(filename)
    elif action == "read":
        filename = input("Enter filename to read: ").strip()
        file_path = BASE_PATH / filename
        if file_path.exists():
            read_file(file_path)
        else:
            print("File not found.")
    elif action == "change editor":
        preferred_editor = pick_editor()
    elif action == "quit":
        print("Goodbye!")
        break
