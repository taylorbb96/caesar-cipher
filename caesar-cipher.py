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
    key = str(mp.pi)
    key = key.replace('.','')
    key_list = []

    for char in key:
        key_list.append(int(char))

    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    input_index = 0
    is_lower = False

    output_str = ''

    for char in input_text:
        if char not in upper_alphabet and char not in upper_alphabet.lower():
            output_str += char
            input_index+=1
            continue
        elif char in upper_alphabet:
            char_index = upper_alphabet.index(char)
        elif char in upper_alphabet.lower():
            char_index = upper_alphabet.lower().index(char)
            is_lower = True

        encoded_index = char_index + key_list[input_index]

        if encoded_index > 25:
            encoded_index -= 26

        encoded_char = upper_alphabet[encoded_index]

        if is_lower:
            is_lower = False
            encoded_char = encoded_char.lower()

        print(f'Key is {key_list[input_index]}')

        output_str += encoded_char

        input_index+=1

    print(output_str)

        

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