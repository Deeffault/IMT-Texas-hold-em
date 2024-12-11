class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.cards = []
        self.active = True  # Display if the player is still in the round   
    
    def bet(self, amount):
        if amount > self.chips:
            raise ValueError("Insufficient amount of chips")
        self.chips -= amount
        return amount

    def fold(self):
        self.active = False