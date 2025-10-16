# main.py
import tkinter as tk
from tkinter import ttk

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 720
BG_COLOR = "#121212"
ACCENT = "#d4af37"  # gold accent


class BaseFrame(tk.Frame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, bg=BG_COLOR, **kwargs)
        self.controller = controller

    def show(self):
        """Bring this frame to the front."""
        self.lift()


class MainMenuFrame(BaseFrame):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        title = tk.Label(self, text="Aulric's Legacy", font=("Cinzel", 36, "bold"),
                         fg=ACCENT, bg=BG_COLOR)
        title.pack(pady=(30, 10))

        btn_frame = tk.Frame(self, bg=BG_COLOR)
        btn_frame.pack(pady=10)

        # Buttons
        pages = [("Battle", "Battle"),
                 ("Shop", "Shop"),
                 ("Inventory", "Inventory"),
                 ("Gear", "Gear"),
                 ("Stats", "Stats"),
                 ("Exit", "Exit")]

        for text, name in pages:
            b = tk.Button(btn_frame, text=text, width=18, height=2,
                          bg="#1f1f1f", fg=ACCENT, font=("Cinzel", 12, "bold"),
                          relief="flat",
                          command=lambda n=name: controller.show_page(n))
            b.pack(pady=6)


class BattleFrame(BaseFrame):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        title = tk.Label(self, text="Battle", font=("Cinzel", 24, "bold"),
                         fg=ACCENT, bg=BG_COLOR)
        title.pack(pady=8)

        # Placeholder content (unfinished)
        placeholder = tk.Label(self, text="(Enemy Finder & Fight Area Placeholder)",
                               bg="#1b1b1b", fg="#dddddd", width=60, height=20,
                               relief="sunken", bd=2)
        placeholder.pack(padx=12, pady=12)


class ShopFrame(BaseFrame):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        title = tk.Label(self, text="Shop", font=("Cinzel", 24, "bold"),
                         fg=ACCENT, bg=BG_COLOR)
        title.pack(pady=8)

        placeholder = tk.Label(self, text="(Shop Overlay Placeholder)",
                               bg="#1b1b1b", fg="#dddddd", width=80, height=20,
                               relief="sunken", bd=2)
        placeholder.pack(padx=12, pady=12)


class InventoryFrame(BaseFrame):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        title = tk.Label(self, text="Inventory", font=("Cinzel", 24, "bold"),
                         fg=ACCENT, bg=BG_COLOR)
        title.pack(pady=8)

        # 4x5 grid placeholder
        grid_frame = tk.Frame(self, bg=BG_COLOR)
        grid_frame.pack(pady=10)

        rows, cols = 4, 5
        for r in range(rows):
            for c in range(cols):
                slot = tk.Label(grid_frame, text="", bg="#1c1c1c", fg="#ddd",
                                width=12, height=6, relief="ridge", bd=2)
                slot.grid(row=r, column=c, padx=6, pady=6)


class GearFrame(BaseFrame):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        title = tk.Label(self, text="Gear", font=("Cinzel", 24, "bold"),
                         fg=ACCENT, bg=BG_COLOR)
        title.pack(pady=8)

        gear_frame = tk.Frame(self, bg=BG_COLOR)
        gear_frame.pack(pady=10)

        slots = ["Weapon", "Helm", "Chest", "Legs", "Boots", "Ring L", "Ring R"]
        for i, name in enumerate(slots):
            slot = tk.Label(gear_frame, text=name, bg="#1c1c1c", fg="#ddd",
                            width=16, height=4, relief="ridge", bd=2)
            slot.grid(row=i, column=0, padx=6, pady=6)


class StatsFrame(BaseFrame):
    def __init__(self, master, controller):
        super().__init__(master, controller)
        title = tk.Label(self, text="Stats", font=("Cinzel", 24, "bold"),
                         fg=ACCENT, bg=BG_COLOR)
        title.pack(pady=8)

        stats_frame = tk.Frame(self, bg=BG_COLOR)
        stats_frame.pack(pady=10)

        # stat labels
        stats = ["HP", "ATK", "DEF", "CRIT", "SPEED"]
        for i, stat in enumerate(stats):
            row = tk.Frame(stats_frame, bg=BG_COLOR)
            row.pack(fill="x", padx=12, pady=6)
            lbl = tk.Label(row, text=f"{stat}: 0", bg=BG_COLOR, fg="#ddd", font=("Arial", 12))
            lbl.pack(side="left")
            plus = tk.Button(row, text="+", width=3, height=1,
                             bg="#2b2b2b", fg=ACCENT, font=("Arial", 10, "bold"),
                             relief="flat")
            plus.pack(side="right")


class RPGGame(tk.Tk):
    """Main application class and frame manager."""
    def __init__(self):
        super().__init__()
        self.title("Aulric's Legacy")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.configure(bg=BG_COLOR)

        # Container for pages
        self.container = tk.Frame(self, bg=BG_COLOR)
        self.container.pack(expand=True, fill="both")

        # frames
        self.frames = {}
        for F, name in [(MainMenuFrame, "MainMenu"),
                        (BattleFrame, "Battle"),
                        (ShopFrame, "Shop"),
                        (InventoryFrame, "Inventory"),
                        (GearFrame, "Gear"),
                        (StatsFrame, "Stats")]:
            frame = F(self.container, controller=self)
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.frames[name] = frame

        # opens main menu
        self.show_page("MainMenu")

        # player icon and level display (placeholder)
        top_bar = tk.Frame(self, bg=BG_COLOR)
        top_bar.place(relx=0, rely=0, relwidth=1, height=60)
        player_icon = tk.Label(top_bar, text="Player", bg="#1b1b1b", fg="#ddd", width=8, height=2, relief="ridge")
        player_icon.pack(side="left", padx=12, pady=8)
        self.level_label = tk.Label(top_bar, text="Lvl 1", bg=BG_COLOR, fg=ACCENT, font=("Cinzel", 12, "bold"))
        self.level_label.pack(side="left", padx=6)

        # shop icon and aulrics counter (placeholder)
        shop_frame = tk.Frame(top_bar, bg=BG_COLOR)
        shop_frame.pack(side="right", padx=12)
        shop_btn = tk.Button(shop_frame, text="Shop", width=8, bg="#1f1f1f", fg=ACCENT,
                             command=lambda: self.show_page("Shop"))
        shop_btn.pack(side="left", padx=6)
        self.aulrics_label = tk.Label(shop_frame, text="Aulrics: 100", bg=BG_COLOR, fg="#ddd")
        self.aulrics_label.pack(side="left", padx=6)
        
        # Closes Gui
    def show_page(self, name: str):
        if name == "Exit":
            self.destroy()
            return
        frame = self.frames.get(name)
        if frame:
            frame.show()
        else:
            print(f"[DEBUG] No frame named {name}")


if __name__ == "__main__":
    app = RPGGame()
    app.mainloop()
