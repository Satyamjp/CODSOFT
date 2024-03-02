from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("To-Do-List Program")
root.geometry("700x700")
my_font = Font(family="Castellar", size=25, weight="bold")
my_frame = Frame(root)
my_frame.pack(pady=10)
my_list = Listbox(my_frame,
                 font=my_font,
                 width=18,
                 height=8,
                 bg="#c2aeaf",
                 fg="black",
                 highlightthickness=5,
                 selectbackground="#36454F",
                 activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)
stuff = ["Hello", "Learn Python"]
for item in stuff:
    my_list.insert(END, item)

my_scroll = Scrollbar(my_frame)
my_scroll.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand=my_scroll.set)
my_scroll.config(command=my_list.yview)

my_entry = Entry(root, width=26, font=("helvetica", 16))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

delete_button = Button(button_frame, text="Delete Item", bg="#e60e19", border=4, padx=8, pady=5, command=delete_item)
add_button = Button(button_frame, text="Add Item", bg='#e60e19', fg="#DDF2FD", border=4, padx=8, pady=5, command=add_item)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)

root.mainloop()
