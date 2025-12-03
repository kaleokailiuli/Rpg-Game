"""Main Class"""

import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow

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
        self.setFixedSize(1200, 800) # Dimensions
        self.player = Player("Hero")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


