"""
Enemy class
enemy stats and rewards
"""
import random

class Enemy:
    """Represents an enemy"""
    
    def __init__(self, name, level, rarity):
        """
        Initialize enemy
        
        Args:
            name: Enemy name
            level: Enemy level
            rarity: 'common', 'rare', 'epic', 'legendary', 'ancestral'
        """
        self.name = name
        self.level = level
        self.rarity = rarity
        
        # Basic Stats
        self.max_hp = random.randint(150, 200) + (level * random.randint(10, 12))
        self.current_hp = self.max_hp
        self.atk = random.randint(25, 35) + (level * random.randint(5, 8))
        
    
    def take_damage(self, damage):
        """Take damage"""
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
    
    def is_alive(self):
        """Checks if enemy is alive"""
        return self.current_hp > 0
    
    def __str__(self):
        """String representation"""
        return (f"{self.name} (Lv.{self.level} {self.rarity.upper()})\n"
                f"HP: {self.current_hp}/{self.max_hp} | ATK: {self.atk}")


if __name__ == '__main__':
    print("Test Enemy\n")
    
    goblin = Enemy("Goblin", 1, "common")
    print(goblin)
    print()
    
    dragon = Enemy("Dragon", 5, "legendary")
    print(dragon)
    print()
    
    print("Goblin takes 30 damage...")
    goblin.take_damage(30)
    print(goblin)