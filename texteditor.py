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