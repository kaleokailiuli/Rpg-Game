"""Main Class"""

import sys
import os

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                               QHBoxLayout, QFrame, QVBoxLayout, QPushButton, QTextEdit)
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
        self.setFixedSize(1200, 800)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main layout
        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

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

        # Battle frame
        self.battle_frame = QFrame(central_widget)
        self.battle_frame.setFixedSize(500, 350)
        self.battle_frame.move(350, 0)  # Position
        self.battle_frame.setStyleSheet(
            "background-color: #2C3E50; border: 2px solid #34495E; border-radius: 10px;"
        )

        battle_layout = QVBoxLayout(self.battle_frame)
        battle_layout.setContentsMargins(20, 20, 20, 20)

        # Battle arena label
        self.arena_label = QLabel("BATTLE ARENA")
        self.arena_label.setAlignment(Qt.AlignCenter)
        self.arena_label.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        battle_layout.addWidget(self.arena_label)

        # Spawn enemy button
        self.spawn_button = QPushButton("Spawn Test Goblin")
        self.spawn_button.setStyleSheet(
            "background-color: #34495E; color: white; border: none; padding: 10px; "
            "font-size: 14px; border-radius: 5px;"
        )
        self.spawn_button.clicked.connect(self.spawn_goblin)
        battle_layout.addWidget(self.spawn_button)

        # Combat log
        self.combat_log = QTextEdit()
        self.combat_log.setReadOnly(True)
        self.combat_log.setMaximumHeight(120)
        self.combat_log.setStyleSheet(
            "background-color: #1a252f; color: #ECF0F1; border: none; "
            "font-family: monospace; font-size: 11px;"
        )
        battle_layout.addWidget(self.combat_log)

        self.show()

    def log(self, message: str):
        """Add a message to the combat log."""
        self.combat_log.append(message)

    def spawn_goblin(self):
        """Create a goblin and show it in the arena."""
        goblin = Enemy("Goblin", 1, "common")
        self.current_enemy = goblin
        self.arena_label.setText(f"⚔️ {goblin.name}\nLv.{goblin.level} {goblin.rarity.upper()}")
        self.log("A Goblin appears!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
