from models.table import Table
from models.player import Player
from utils.display import display_table, display_card
from treys import Evaluator, Card

def main():
    table = Table()
    players = [Player("Alice", 100), Player("Bob", 100)]
    
    table.shuffle_package()
    
    for player in players:
        table.distribute_cards(player)
        
    table.distribute_common_cards(3)  # Flop
    display_table(table)
    
    table.distribute_common_cards(1)  # Turn
    display_table(table)
    
    table.distribute_common_cards(1)  # River
    display_table(table)
    
    for player in players:
        print(f"{player.name} cards: {display_card(player.cards)}")
    
    evaluator = Evaluator()
    best_hand = None
    winner = None
    
    suit_map = {'Hearts': 'h', 'Diamonds': 'd', 'Clubs': 'c', 'Spades': 's'}
    rank_map = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': 'T', 'J': 'J', 'Q': 'Q', 'K': 'K', 'A': 'A'}
    
    for player in players:
        player_hand = [Card.new(rank_map[card.value] + suit_map[card.suit]) for card in player.cards]
        common_hand = [Card.new(rank_map[card.value] + suit_map[card.suit]) for card in table.common_cards]
        score = evaluator.evaluate(common_hand, player_hand)
        if best_hand is None or score < best_hand:
            best_hand = score
            winner = player
    
    print(f"The winner is {winner.name} with a score of {best_hand}")
        
if __name__ == "__main__":
    main()