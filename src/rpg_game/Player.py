"""
Player class
player stats, leveling, and inventory
"""

# might add more features later


class Player:
    """Represents the player character"""
    
    def __init__(self, name="Hero"):
        """base stats"""
        self.name = name
        self.level = 1
        self.exp = 0
        self.keys = 0
        
        # Base stats
        self.base_hp = 200
        self.base_atk = 50
        self.base_def = 10
        self.base_speed = 5
        self.base_crit = 1
        
        self.current_hp = self.base_hp
        
        # prolly will add inventory and equipment later
        self.inventory = []
    
    def take_damage(self, damage):
        """Take damage"""
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
    
    def is_alive(self):
        """Checks if Player is alive"""
        return self.current_hp > 0
    
    def __str__(self):
        """String representation of player"""
        return (f"{self.name} - Level {self.level}\n"
                f"HP: {self.current_hp}/{self.base_hp} | ATK: {self.base_atk} | "
                f"DEF: {self.base_def}% | Speed: {self.base_speed}% | Crit: {self.base_crit}%\n"
                f"Keys: {self.keys}")


if __name__ == '__main__':
    print("Testing Player\n")
    
    player = Player("Hero")
    print(player)
    print()
    
    print("Taking 30 damage...")
    player.take_damage(30)
    print(player)