import tkinter as tk
from tkinter import filedialog, messagebox

def newfile():
    text.delete(1.0, tk.END)

def openfile():
    file_path = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END,file.read())

def savefile():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path,'w') as file:
            file.write(text.get(1.0,tk.END))
            messagebox.showinfo("Info","Files saves successfully")
            
root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New", command=newfile)
file_menu.add_command(label="Open", command=openfile)
file_menu.add_command(label="Save", command=savefile)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root,wrap=tk.WORD, font=("Helvetica",12), fg="black")
text.pack(expand=tk.YES,fill=tk.BOTH)

root.mainloop()


