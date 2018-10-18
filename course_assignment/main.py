import matplotlib
matplotlib.use('TkAgg')
from window import Window
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("DE Course Assignment")
    window = Window(root)
    tk.mainloop()
