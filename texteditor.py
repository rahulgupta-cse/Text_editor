# Import required libraries
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to create a new file (clear text area)
def newfile():
    text.delete(1.0, tk.END)

# Function to open an existing file
def openfile():
    # Open file dialog to select a .txt file
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    # If a file is selected
    if file_path:
        with open(file_path, "r") as file: # for open the file
            text.delete(1.0, tk.END)  # Clear existing text
            text.insert(tk.END, file.read())  # Insert file content

# Function to save the file
def savefile():
    # Open save dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", # add txt as extension for file name
        filetypes=[("Text Files", "*.txt")]
    )
    # If a file path is provided
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))  # Write text content
        
        # Show confirmation message
        messagebox.showinfo("Info", "File saved successfully")

# Create main window
root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

# Create menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# Create File menu
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

# Add menu options
file_menu.add_command(label="New", command=newfile)
file_menu.add_command(label="Open", command=openfile)
file_menu.add_command(label="Save", command=savefile)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create text area widget
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 12),
    fg="black"
)

# Make text area expand with window
text.pack(expand=tk.YES, fill=tk.BOTH)

# Run the application
root.mainloop()