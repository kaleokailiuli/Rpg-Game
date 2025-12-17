"""Main Class"""

import sys
import os

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                               QHBoxLayout, QFrame, QVBoxLayout, QPushButton, QTextEdit, QGridLayout)
from PySide6.QtCore import Qt
from Player import Player
from Enemy import Enemy
from Gear import Gear
from Coin import Coin
from Stats import Stats

class MainWindow(QMainWindow):
    """Main game window."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPG Game")
        self.setFixedSize(1200, 850) 

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(20)

        # Player icon
        self.player_icon_label = QLabel("🧙‍♂️ Level 1", central_widget)
        self.player_icon_label.setFixedSize(140, 50)
        self.player_icon_label.move(1050, 10)
        self.player_icon_label.setStyleSheet("""
            font-size: 20px;
            padding: 8px;
            background: rgba(0,0,0,0.8);
            border-radius: 8px;
            color: white;
            border: 2px solid #34495E;
        """)

        # battle system values
        self.player = Player("Hero")
        self.current_enemy = None

        self.left_column = QFrame(central_widget)
        left_layout = QVBoxLayout(self.left_column)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(10)

        # Inventory panel
        self.inventory_frame = QFrame(self.left_column)
        self.inventory_frame.setStyleSheet(
            "background-color: #34495E; border: 2px solid #2C3E50; border-radius: 3px;"
        )

        inventory_layout = QVBoxLayout(self.inventory_frame)
        inventory_layout.setContentsMargins(10, 10, 10, 10)

        inv_label = QLabel("INVENTORY")
        inv_label.setAlignment(Qt.AlignCenter)
        inv_label.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        inventory_layout.addWidget(inv_label)

        grid = QGridLayout()
        grid.setSpacing(5)
        inventory_layout.addLayout(grid)

        self.inventory_slots = []
        for r in range(5):  # 5 rows
            for c in range(4):  # 4 columns
                slot = QFrame(self.inventory_frame)
                slot.setFixedSize(50, 50)
                slot.setStyleSheet(
                    "background-color: #2C3E50; border: 1px solid #7F8C8D; border-radius: 4px;"
                )
                grid.addWidget(slot, r, c)
                self.inventory_slots.append(slot)

        left_layout.addWidget(self.inventory_frame)

        # stats panel
        self.stats_frame = QFrame(self.left_column)
        self.stats_frame.setStyleSheet(
            "background-color: #34495E; border: 2px solid #2C3E50; border-radius: 10px;"
        )

        stats_layout = QVBoxLayout(self.stats_frame)
        stats_layout.setContentsMargins(10, 10, 10, 10)
        stats_layout.setSpacing(5)

        stats_title = QLabel("PLAYER STATS")
        stats_title.setAlignment(Qt.AlignCenter)
        stats_title.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        stats_layout.addWidget(stats_title)

        # Stat Labels w button
        self.hp_label = QLabel(f"HP: {self.player.current_hp}/{self.player.base_hp}")
        hp_plus = QPushButton("+")
        hp_plus.setFixedSize(25, 25)
        hp_plus.setStyleSheet("background: green; color: white; border: none; font-weight: bold;")
        stats_layout.addWidget(self.hp_label)
        stats_layout.addWidget(hp_plus)

        self.atk_label = QLabel(f"ATK: {self.player.base_atk}")
        atk_plus = QPushButton("+")
        atk_plus.setFixedSize(25, 25)
        atk_plus.setStyleSheet("background: green; color: white; border: none; font-weight: bold;")
        stats_layout.addWidget(self.atk_label)
        stats_layout.addWidget(atk_plus)

        self.def_label = QLabel(f"DEF: {self.player.base_def}%")
        def_plus = QPushButton("+")
        def_plus.setFixedSize(25, 25)
        def_plus.setStyleSheet("background: green; color: white; border: none; font-weight: bold;")
        stats_layout.addWidget(self.def_label)
        stats_layout.addWidget(def_plus)

        self.speed_label = QLabel(f"Speed: {self.player.base_speed}%")
        speed_plus = QPushButton("+")
        speed_plus.setFixedSize(25, 25)
        speed_plus.setStyleSheet("background: green; color: white; border: none; font-weight: bold;")
        stats_layout.addWidget(self.speed_label)
        stats_layout.addWidget(speed_plus)

        self.crit_label = QLabel(f"Crit: {self.player.base_crit}%")
        crit_plus = QPushButton("+")
        crit_plus.setFixedSize(25, 25)
        crit_plus.setStyleSheet("background: green; color: white; border: none; font-weight: bold;")
        stats_layout.addWidget(self.crit_label)
        stats_layout.addWidget(crit_plus)

        self.reset_stats_button = QPushButton("Reset Stats")
        self.reset_stats_button.setStyleSheet(
            "background-color: #7F8C8D; color: white; border: none; padding: 8px; "
            "font-size: 13px; border-radius: 5px;"
        )
        stats_layout.addWidget(self.reset_stats_button)

        left_layout.addWidget(self.stats_frame)

        # Battle Arena
        center_column = QFrame(central_widget)
        center_layout = QVBoxLayout(center_column)
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(10)
        center_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        self.battle_frame = QFrame(center_column)
        self.battle_frame.setFixedSize(500, 300)  
        self.battle_frame.setStyleSheet(
            "background-color: #2C3E50; border: 2px solid #34495E; border-radius: 10px;"
        )

        battle_layout = QVBoxLayout(self.battle_frame)
        battle_layout.setContentsMargins(20, 20, 20, 20)

        self.arena_label = QLabel("BATTLE ARENA")
        self.arena_label.setAlignment(Qt.AlignCenter)
        self.arena_label.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        battle_layout.addWidget(self.arena_label)

        self.spawn_button = QPushButton("Spawn Test Goblin")
        self.spawn_button.setStyleSheet(
            "background-color: #34495E; color: white; border: none; padding: 10px; "
            "font-size: 14px; border-radius: 5px;"
        )
        self.spawn_button.clicked.connect(self.spawn_goblin)
        battle_layout.addWidget(self.spawn_button)

        self.attack_button = QPushButton("Attack")
        self.attack_button.setStyleSheet(
            "background-color: #8B0A0A; color: white; border: none; padding: 10px; "
            "font-size: 14px; border-radius: 5px;"
        )
        self.attack_button.clicked.connect(self.player_attack)
        battle_layout.addWidget(self.attack_button)

        self.combat_log = QTextEdit()
        self.combat_log.setReadOnly(True)
        self.combat_log.setMaximumHeight(120)
        self.combat_log.setStyleSheet(
            "background-color: #1a252f; color: #ECF0F1; border: none; "
            "font-family: monospace; font-size: 11px;"
        )
        battle_layout.addWidget(self.combat_log)

        center_layout.addWidget(self.battle_frame)

        main_layout.addWidget(self.left_column)
        main_layout.addWidget(center_column)

        self.show()

    def log(self, message: str):
        """Add a message to the combat log."""
        self.combat_log.append(message)

    def spawn_goblin(self):
        """Create a goblin and show it in the arena."""
        goblin = Enemy("Goblin", 1, "common")
        self.current_enemy = goblin
        self.arena_label.setText(f" {goblin.name}\nLv.{goblin.level} {goblin.rarity.upper()}\nHP: {goblin.max_hp}/{goblin.max_hp}")
        self.log("A Goblin appears!")

    def player_attack(self):
        if self.current_enemy is not None: #checks to see if there is an enemy spawned alkready
            self.current_enemy.take_damage(self.player.base_atk)
            self.log(f"You attacked {self.current_enemy.name} for {self.player.base_atk} damage!")
            self.arena_label.setText(f" {self.current_enemy.name}\nLv.{self.current_enemy.level} {self.current_enemy.rarity.upper()}\nHP: {self.current_enemy.current_hp}/{self.current_enemy.max_hp}")
            if not self.current_enemy.is_alive():
                self.log(f"You killed {self.current_enemy.name}!")
                self.current_enemy = None
                self.arena_label.setText("BATTLE ARENA")
            else:
                self.enemy_attack()
        else:
            self.log("No enemy to attack!")

    def enemy_attack(self):
        if self.current_enemy is not None:
            self.player.take_damage(self.current_enemy.atk)
            self.log(f"{self.current_enemy.name} hit you for {self.current_enemy.atk} damage!")
            self.hp_label.setText(f"HP: {self.player.current_hp}/{self.player.base_hp}")
            if not self.player.is_alive():
                self.log("You died!")
                self.current_enemy = None
                self.arena_label.setText("BATTLE ARENA")
                self.player.current_hp = self.player.base_hp
                self.hp_label.setText(f"HP: {self.player.current_hp}/{self.player.base_hp}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())