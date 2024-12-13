class Card:
    """
    Represents a playing card with a value and suit.
    """
    def __init__(self, value, suit):
        """
        Initializes a Card object.

        Args:
            value (str): The value of the card (e.g., '2', 'K', 'A').
            suit (str): The suit of the card (e.g., 'Hearts', 'Spades').
        """
        self.value = value
        self.suit = suit
        
    def __repr__(self):
        """
        Returns a string representation of the card.

        Returns:
            str: The string representation of the card.
        """
        return f"{self.value} of {self.suit}"