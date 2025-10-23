"""
Gear class for RPG game
Handles equipment items
"""


class Gear:
    """Represents an equipment item"""
    
    def __init__(self, name, gear_type, rarity, stats):
        """
        Initialize gear
        
        Args:
            name: Gear name
            gear_type: 'helm', 'chest', 'legs', 'boots', 'ring'
            rarity: 'common', 'rare', 'epic', 'legendary', 'ancestral'
            stats: Dictionary like {'hp': 10, 'atk': 5}
        """
        self.name = name
        self.gear_type = gear_type
        self.rarity = rarity
        self.stats = stats
    
    def __str__(self):
        """String representation"""
        stat_str = ', '.join([f"{k.upper()}: {v:+d}" for k, v in self.stats.items()])
        return f"[{self.rarity.upper()}] {self.name} ({self.gear_type}) - {stat_str}"


if __name__ == '__main__':
    print("=== Testing Gear ===\n")
    
    helmet = Gear("Iron Helmet", "helm", "common", {'hp': 10, 'def': 2})
    sword_ring = Gear("Sword Ring", "ring", "rare", {'atk': 15, 'crit': 3})
    
    print(helmet)
    print(sword_ring)