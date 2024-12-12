class Player:
    """
    Represents a player in the game.
    """
    def __init__(self, name, chips):
        """
        Initializes a Player object.

        Args:
            name (str): The name of the player.
            chips (int): The number of chips the player has.
        """
        self.name = name
        self.chips = chips
        self.cards = []
        self.active = True  # Display if the player is still in the round   
    
    def bet(self, amount):
        """
        Places a bet by the player.

        Args:
            amount (int): The amount to bet.

        Returns:
            int: The amount bet.

        Raises:
            ValueError: If the bet amount is invalid.
        """
        if amount > self.chips:
            raise ValueError("Insufficient amount of chips")
        if amount <= 0:
            raise ValueError("Bet amount must be positive")
        self.chips -= amount
        return amount

    def fold(self):
        """
        Folds the player's hand, making them inactive for the round.
        """
        self.active = False

    def is_eliminated(self):
        """
        Checks if the player is eliminated from the game.

        Returns:
            bool: True if the player is eliminated, False otherwise.
        """
        return self.chips <= 0

    def add_card(self, card):
        """
        Adds a card to the player's hand.

        Args:
            card (Card): The card to add.
        """
        self.cards.append(card)