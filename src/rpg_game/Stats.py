"""
Stats class for RPG game
Handles stat storage
"""

#stores stats


class Stats:
    """Represents a collection of stats"""

    def __init__(self, hp=0, atk=0, defense=0, speed=0, crit=0):
        """
        Initialize stats
        
        Args:
            hp: Health points
            atk: Attack damage
            defense: Block chance percentage
            speed: Dodge chance percentage
            crit: Critical hit chance percentage
        """
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.speed = speed
        self.crit = crit

    def __str__(self):
        # Display
        return (f"HP: {self.hp} | ATK: {self.atk} | DEF: {self.defense}% | "
                f"Speed: {self.speed}% | Crit: {self.crit}%")


if __name__ == '__main__':
    # stats
    print("Testing Stats\n")
    
    player_stats = Stats(hp=100, atk=50, defense=10, speed=5, crit=1)
    enemy_stats = Stats(hp=75, atk=30, defense=8, speed=3, crit=2)
    
    print("Player Stats:")
    print(player_stats)
    # adds gap
    print()
    
    print("Enemy Stats:")
    print(enemy_stats)