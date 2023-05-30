import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
from mpmath import mp

def read_file(root):
        file = askopenfile(parent=root, mode='r', title="Choose a file", filetypes=[("TXT file", "*.txt")])
        if file:
            return file.read()

def encode(root, encode_text):
    encode_text.set("loading...")
    input_text = read_file(root)

    if not input_text:
        error_win = tk.Toplevel(root)
        error_win.geometry("500x200")
        error_win.title('Error')
        tk.Label(error_win, text="Failed to Encode\n Either the file contains no valid data, or no file was selected",font="Raleway").place(x=5,y=80)
        encode_text.set("Encode")
        return

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

        output_str += encoded_char

        input_index+=1

    print(output_str)

    with open('encoded.txt','w') as output_file:
        output_file.write(output_str)

    response = tk.Toplevel(root)
    response.geometry("500x200")
    response.title('Success')
    response_text = tk.Label(response, text="Selected File Encoded",font="Raleway").place(x=150,y=80)

    encode_text.set("Encode")

def decode(root, decode_text):
    decode_text.set("loading...")

    decode_text.set("Decode")

def main():
    root = tk.Tk()

    canvas = tk.Canvas(root, width=650, height=300)
    canvas.grid(columnspan=3, rowspan=3)

    instructions = tk.Label(root, text="Select whether you would like to encode or decode a file, then select that file", font="Raleway")
    instructions.grid(columnspan=3, column=0, row=0)

    #browse button
    encode_text = tk.StringVar()
    encode_btn = tk.Button(root, textvariable=encode_text, command=lambda:encode(root, encode_text), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
    encode_text.set("Encode")
    encode_btn.grid(column=1, row=1)

    decode_text = tk.StringVar()
    decode_btn = tk.Button(root, textvariable=decode_text, command=lambda:decode(root, decode_text), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
    decode_text.set("Decode")
    decode_btn.grid(column=1, row=2)

    canvas = tk.Canvas(root, width=600, height=250)
    canvas.grid(columnspan=3)

    root.mainloop()


if __name__ == '__main__':
    main()