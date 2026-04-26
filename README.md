Simple Tkinter Text Editor

A lightweight desktop text editor built using Python’s built-in Tkinter library. It allows users to create, open, edit, and save .txt files with a simple graphical interface.

Features
Create new text files
Open existing .txt files
Save files easily
Simple and clean GUI
Auto-expanding text area
Built-in menu bar (File operations)
Requirements
Python 3.x
Tkinter (usually included with Python by default)

To check Tkinter availability:

python -m tkinter
How to Run
Save the script as text_editor.py
Open terminal or command prompt
Run the script:
python text_editor.py
File Structure
text-editor/
│
├── text_editor.py
└── README.md
How It Works

The application uses:

tkinter.Text → Main text editing area
tkinter.Menu → File menu (New, Open, Save, Exit)
filedialog → To open/save files
messagebox → To show confirmation messages
Menu Options
File Menu
New → Clears the text area
Open → Opens a .txt file and loads content
Save → Saves current text to a file
Exit → Closes the application
UI Overview
Large resizable text area
Simple top menu bar
Clean and minimal interface
Future Improvements
Add Copy, Cut, Paste functionality
Add Dark Mode
Add font customization
Add word count feature
Add tabbed editing support

Author

Rahul Gupta
