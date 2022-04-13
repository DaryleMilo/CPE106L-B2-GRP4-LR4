import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo

root = tkinter.Tk()
root.title('Tkinter File Reader')
root.resizable(True, True)
root.geometry('500x300')

def select_file():

    target=filedialog.askopenfilename() 
    for line in open(target):
        print(line, end='')

    showinfo(
        title='Selected File',
        message=target
    )

open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)

root.mainloop()