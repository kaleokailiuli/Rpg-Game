
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                                QHBoxLayout, QLabel, QPushButton, QTextEdit)
from PySide6.QtCore import Qt
import sys


class GameGUI(QMainWindow):
    """Main game window"""
    
    def __init__(self):
        """Initialize the GUI"""
        super().__init__()
        self.setWindowTitle("RPG Game")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        
        # Left side - Stats
        self.create_left_panel(main_layout)
        
        # Center - Battle area and log
        self.create_center_panel(main_layout)
        
        # Right side - Inventory and equipment
        self.create_right_panel(main_layout)
    
    def create_left_panel(self, main_layout):
        """Create left panel with stats"""
        left_panel = QVBoxLayout()
        
        # Stats label
        stats_label = QLabel("PLAYER STATS")
        stats_label.setAlignment(Qt.AlignCenter)
        left_panel.addWidget(stats_label)
        
        # Stat displays (placeholder for now)
        self.hp_label = QLabel("HP: 100/100")
        self.atk_label = QLabel("ATK: 50")
        self.def_label = QLabel("DEF: 10%")
        self.speed_label = QLabel("Speed: 5%")
        self.crit_label = QLabel("Crit: 1%")
        
        left_panel.addWidget(self.hp_label)
        left_panel.addWidget(self.atk_label)
        left_panel.addWidget(self.def_label)
        left_panel.addWidget(self.speed_label)
        left_panel.addWidget(self.crit_label)
        
        # Reset stats button
        reset_button = QPushButton("Reset Stats")
        left_panel.addWidget(reset_button)
        
        left_panel.addStretch()
        main_layout.addLayout(left_panel, 1)
    
    def create_center_panel(self, main_layout):
        """Create center panel with battle screen and log"""
        center_panel = QVBoxLayout()
        
        # Battle screen (placeholder)
        battle_label = QLabel("BATTLE SCREEN")
        battle_label.setAlignment(Qt.AlignCenter)
        battle_label.setMinimumHeight(400)
        battle_label.setStyleSheet("background-color: #2C3E50; color: white;")
        center_panel.addWidget(battle_label)
        
        # Combat log
        log_label = QLabel("Combat Log:")
        center_panel.addWidget(log_label)
        
        self.combat_log = QTextEdit()
        self.combat_log.setReadOnly(True)
        self.combat_log.setMaximumHeight(200)
        center_panel.addWidget(self.combat_log)
        
        main_layout.addLayout(center_panel, 2)
    
    def create_right_panel(self, main_layout):
        """Create right panel with inventory and equipment"""
        right_panel = QVBoxLayout()
        
        # Player icon and level (placeholder)
        player_info = QHBoxLayout()
        player_icon = QLabel("👤")
        player_level = QLabel("Level: 1")
        player_info.addWidget(player_icon)
        player_info.addWidget(player_level)
        right_panel.addLayout(player_info)
        
        # Inventory label
        inventory_label = QLabel("INVENTORY")
        inventory_label.setAlignment(Qt.AlignCenter)
        right_panel.addWidget(inventory_label)
        
        # Inventory(placeholder)
        inventory_placeholder = QLabel("Inventory Grid\n(4x5)")
        inventory_placeholder.setAlignment(Qt.AlignCenter)
        inventory_placeholder.setMinimumHeight(200)
        inventory_placeholder.setStyleSheet("background-color: #34495E; color: white;")
        right_panel.addWidget(inventory_placeholder)
        
        # Equipment
        equipment_label = QLabel("EQUIPMENT")
        equipment_label.setAlignment(Qt.AlignCenter)
        right_panel.addWidget(equipment_label)
        
        # Equipment slots (placeholder)
        equipment_placeholder = QLabel("Helm\nChest\nLegs\nBoots\nRing1\nRing2")
        equipment_placeholder.setAlignment(Qt.AlignCenter)
        equipment_placeholder.setMinimumHeight(200)
        equipment_placeholder.setStyleSheet("background-color: #34495E; color: white;")
        right_panel.addWidget(equipment_placeholder)
        
        right_panel.addStretch()
        main_layout.addLayout(right_panel, 1)
    
    def add_to_log(self, message):
        """Add message to combat log"""
        self.combat_log.append(message)


def main():
    """Main entry point for the game"""
    app = QApplication(sys.argv)
    window = GameGUI()
    window.show()
    
    # Test adding to log
    window.add_to_log("Game Opened")
    window.add_to_log("Welcome")
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()