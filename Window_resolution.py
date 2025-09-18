import tkinter as tk
import random 

def change_resolution(width, height):
    root.geometry(f"{width}x{height}")

def print_random_number():
    number = random.randint(1, 100)
    print(f"Random number: {number}")

root = tk.Tk()
root.title("Resizable Window")
root.geometry("640x480")

menubar = tk.Menu(root)
root.config(menu=menubar)

view_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=view_menu)

resolutions = [
    ("640 x 480", 640, 480),
    ("800 x 600", 800, 600),
    ("1024 x 768", 1024, 768),
    ("1280 x 720", 1280, 720),
    ("1920 x 1080", 1920, 1080)
]

for label, w, h in resolutions:
    view_menu.add_command(label=label, command=lambda w=w, h=h: change_resolution(w, h))

view_menu.add_separator()
view_menu.add_command(label="Exit", command=root.quit)

random_button = tk.Button(root, text="Print Random Number", command=print_random_number)
random_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()