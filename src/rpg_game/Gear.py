"""
Gear class for RPG game
Handles equipment items
"""

# maybe later make subclasses for weapons or armor
# stats are fixed, might add scaling later

class Gear:
    """Represents an item"""

    def __init__(self, name, gear_type, rarity, stats):
        """
        Initialize gear
        
        Args:
            name: Gear name
            gear_type: 'helm', 'chest', 'legs', 'boots', 'ring'
            rarity: 'common', 'rare', 'epic', 'legendary', 'ancestral, divine'
            stats: Dictionary like {'hp': 10, 'atk': 5}
        """
        # might add checks here for allowed types or rarities
        self.name = name
        self.gear_type = gear_type
        self.rarity = rarity
        self.stats = stats  # stores all item stats
        
        # maybe add level or id later if we need saving

    def __str__(self):
        """Pretty print gear info"""
        # change format later if we want percent stats or bonuses
        stat_str = ', '.join([f"{k.upper()}: {v:+d}" for k, v in self.stats.items()])
        return f"[{self.rarity.upper()}] {self.name} ({self.gear_type}) - {stat_str}"


if __name__ == '__main__':
    # test to see how it looks
    print("Testing Gear\n")
    
    helmet = Gear("Iron Helmet", "helm", "common", {'hp': 10, 'def': 2})
    sword_ring = Gear("Sword Ring", "ring", "rare", {'atk': 15, 'crit': 3})
    sword = Gear("Sword", "sword", "common", {'atk': 1, 'crit': 1})
    Heavens_Spear = Gear("Heavens Spear", "Spear", "divine", {'atk': 100, 'crit': 300})
    Mjolnir = Gear("Mjolnir", "Hammer", "divine", {'atk': 150, 'crit': 200, 'def': 99})
    
    print(helmet)
    print(sword_ring)
    print(sword)
    print(Heavens_Spear)
    print(Mjolnir)
