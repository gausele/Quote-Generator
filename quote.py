import random
import tkinter as tk

with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = [line.replace("–", "-").replace("—", "-").strip() for line in f if line.strip()]


# print(squote)

root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("600x200")

top_frame = tk.Frame(root, bg="lightblue", height=100)
top_frame.pack(fill="x")
top_frame.pack_propagate(False)

label = tk.Label(top_frame, text = "Generate quote to Start", font=("Arial", 14), justify="center", wraplength=550)
label.pack(expand=True)


def qgen(): 
    squote = random.choice(quotes)
    label.config(text = squote)

button = tk.Button(root, text = "Generate Quote", command=qgen)

button.pack(pady=20)

copyright_label = tk.Label(root, text="Made by Utkarsha, 2025, 12:50 PM", font=("Times New Roman", 7), justify="left")
copyright_label.pack()

root.mainloop()