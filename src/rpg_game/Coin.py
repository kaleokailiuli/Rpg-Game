"""
Coin class
Handles currency
"""

class Coin:
    """Represents a currency drop"""

    def __init__(self, amount, source="Unknown"):
        """
        Initialize coin drop
        
        Args:
            amount: Number of coins
            source: Where the coins came from (enemy name, or misc)
        """
        self.amount = amount
        self.source = source
        
        # might add multiplicatives or % based increases in coins

    def __str__(self):
        """Pretty print coin info"""
        # Display format
        return f"{self.amount} Keys from {self.source}"


if __name__ == '__main__':
    # print
    print("Testing Coins\n")
    
    goblin_drop = Coin(10, "Goblin")
    dragon_drop = Coin(500, "Dragon")
    admin_coins = Coin(999999, "Admin Command")
    
    print(goblin_drop)
    print(dragon_drop)
    print(admin_coins)