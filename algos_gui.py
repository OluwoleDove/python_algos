import tkinter as tk
from tkinter import messagebox

# Import the algorithms from your script
from my_py_algos import even_odd, multi_five, char_tri, determine_palindrome, find_prefix

def show_result(result):
    messagebox.showinfo("Result", result)

def calculate_even_odd():
    i = int(entry_i.get())
    j = int(entry_j.get())
    result = even_odd(i, j)
    show_result(result)

def calculate_multi_five():
    n = int(entry_multi_five.get())
    result = multi_five(n)
    show_result(result)

def calculate_char_tri():
    char = entry_char.get()
    lim = int(entry_lim.get())
    result = char_tri(char, lim)
    show_result(result)

def calculate_palindrome():
    palindrome = entry_palindrome.get()
    result = determine_palindrome(palindrome)
    show_result(result)

def calculate_prefix():
    word_list = entry_word_list.get()
    word_list = word_list.split(',')
    result = find_prefix(word_list)
    show_result(result)

# Create the main Tkinter window
root = tk.Tk()
root.title("Algorithms GUI")

# Even/Odd Algorithm
frame_even_odd = tk.Frame(root)
frame_even_odd.pack(fill=tk.X, padx=10)
label_i = tk.Label(frame_even_odd, text="Enter the first integer:")
label_i.pack(side=tk.LEFT)
entry_i = tk.Entry(frame_even_odd)
entry_i.pack(side=tk.LEFT)
label_j = tk.Label(frame_even_odd, text="Enter the second integer:")
label_j.pack(side=tk.LEFT)
entry_j = tk.Entry(frame_even_odd)
entry_j.pack(side=tk.LEFT)
btn_even_odd = tk.Button(frame_even_odd, text="Calculate Even/Odd", command=calculate_even_odd)
btn_even_odd.pack()

# Multi_Five Algorithm
frame_multi_five = tk.Frame(root)
frame_multi_five.pack(fill=tk.X, padx=10)
label_multi_five = tk.Label(frame_multi_five, text="Enter an integer:")
label_multi_five.pack(side=tk.LEFT)
entry_multi_five = tk.Entry(frame_multi_five)
entry_multi_five.pack(side=tk.LEFT)
btn_multi_five = tk.Button(frame_multi_five, text="Calculate Multi_Five", command=calculate_multi_five)
btn_multi_five.pack()

# Char_Tri Algorithm
frame_char_tri = tk.Frame(root)
frame_char_tri.pack(fill=tk.X, padx=10)
label_char = tk.Label(frame_char_tri, text="Enter a character:")
label_char.pack(side=tk.LEFT)
entry_char = tk.Entry(frame_char_tri)
entry_char.pack(side=tk.LEFT)
label_lim = tk.Label(frame_char_tri, text="Enter an integer:")
label_lim.pack(side=tk.LEFT)
entry_lim = tk.Entry(frame_char_tri)
entry_lim.pack(side=tk.LEFT)
btn_char_tri = tk.Button(frame_char_tri, text="Calculate Char_Tri", command=calculate_char_tri)
btn_char_tri.pack()

# Determine_Palindrome Algorithm
frame_palindrome = tk.Frame(root)
frame_palindrome.pack(fill=tk.X, padx=10)
label_palindrome = tk.Label(frame_palindrome, text="Enter a word:")
label_palindrome.pack(side=tk.LEFT)
entry_palindrome = tk.Entry(frame_palindrome)
entry_palindrome.pack(side=tk.LEFT)
btn_palindrome = tk.Button(frame_palindrome, text="Check Palindrome", command=calculate_palindrome)
btn_palindrome.pack()

# Find_Prefix Algorithm
frame_prefix = tk.Frame(root)
frame_prefix.pack(fill=tk.X, padx=10)
label_word_list = tk.Label(frame_prefix, text="Enter a comma-separated list:")
label_word_list.pack(side=tk.LEFT)
entry_word_list = tk.Entry(frame_prefix)
entry_word_list.pack(side=tk.LEFT)
btn_prefix = tk.Button(frame_prefix, text="Find Prefix", command=calculate_prefix)
btn_prefix.pack()

# Run the Tkinter main loop
root.mainloop()