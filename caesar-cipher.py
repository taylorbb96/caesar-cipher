import tkinter as tk
from tkinter.filedialog import askopenfile
from mpmath import mp

def read_file(root):
        file = askopenfile(parent=root, mode='r', title="Choose a file", filetypes=[("TXT file", "*.txt")])
        if file:
            return file.read()

def encode(root, browse_text):
    browse_text.set("loading...")
    input_text = read_file(root)
    mp.dps = len(input_text) + 1
    key_str = str(mp.pi)
    key = []

    #remove decimal
    for char in key_str:
        if char != '.':
            key.append(char)
        continue

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


    for char in input_text:
        if char not in alphabet and lower(char) not in alphabet:
            continue
        elif char not in alphabet

    browse_text.set("Browse")

def main():
    root = tk.Tk()

    canvas = tk.Canvas(root, width=600, height=300)
    canvas.grid(columnspan=3, rowspan=3)

    instructions = tk.Label(root, text="Select whether you would like to encode or decode a file, then select that file", font="Raleway")
    instructions.grid(columnspan=3, column=0, row=0)

    #browse button
    browse_text = tk.StringVar()
    browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:encode(root, browse_text), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
    browse_text.set("Browse")
    browse_btn.grid(column=1, row=1)

    browse_text = tk.StringVar()
    browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:encode(root, browse_text), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
    browse_text.set("Browse")
    browse_btn.grid(column=1, row=2)

    canvas = tk.Canvas(root, width=600, height=250)
    canvas.grid(columnspan=3)

    root.mainloop()


if __name__ == '__main__':
    main()