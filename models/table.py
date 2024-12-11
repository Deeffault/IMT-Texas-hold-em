import random
from models.card import Card

class Table:
    def __init__(self):
        self.common_cards = []
        self.blind = 0
        self.package = self.create_package()

    def create_package(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        return [Card(value, suit) for value in values for suit in suits]

    def shuffle_package(self):
        random.shuffle(self.package)
        
    def distribute_cards(self, player, number=2):
        for _ in range(number):
            player.cards.append(self.package.pop())
            
    def distribute_common_cards(self, number=1):
        for _ in range(number):
            self.common_cards.append(self.package.pop())