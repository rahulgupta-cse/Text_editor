# Import required libraries
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to create a new file (clear text area)
def newfile():
    text.delete(1.0, tk.END)