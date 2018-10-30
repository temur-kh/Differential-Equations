import matplotlib
matplotlib.use('TkAgg')
from window import ApplicationWindow
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("DE Course Assignment")
    window = ApplicationWindow(root)
    window.pack()
    tk.mainloop()
