import tkinter as tk

class RPGApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG Game")
        self.root.geometry("900x600")  # width x height
        self.root.configure(bg="#1a1a1a")  # dark background

        # Just a placeholder label for now
        title = tk.Label(
            self.root,
            text="RPG Game GUI",
            font=("Georgia", 24, "bold"),
            fg="white",
            bg="#1a1a1a"
        )
        title.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = RPGApp(root)
    root.mainloop()
