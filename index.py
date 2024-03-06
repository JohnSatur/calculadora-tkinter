import tkinter as tk
from src.view import View

def main():
    root = tk.Tk()
    app = View(master=root)
    app.master.mainloop()

if __name__ == "__main__":
    main()
