import tkinter as tk
from tkinter import simpledialog
ROOT = tk.Tk()
ROOT.withdraw()
User_INP = simpledialog.askstring(title="Chat-GPT version T.0", prompt="Hi!! What would you like to ask me or talk about ?")
print(User_INP)