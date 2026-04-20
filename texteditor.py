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
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)  # Clear existing text
            text.insert(tk.END, file.read())  # Insert file content

# Function to save the file
def savefile():
    # Open save dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
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