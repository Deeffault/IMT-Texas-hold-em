import os
import time
from models import Table, Player
from utils.display import display_table, display_card
from treys import Evaluator, Card
from colorama import Fore, Style, init

init()

def clear_terminal():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def shuffle_animation():
    """
    Displays a shuffling animation in the terminal.
    """
    print(Fore.YELLOW + "Shuffling the cards" + Style.RESET_ALL, end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

def deal_card_animation(player_name, card):
    """
    Displays a card dealing animation in the terminal.

    Args:
        player_name (str): The name of the player receiving the card.
        card (Card): The card being dealt.
    """
    print(Fore.CYAN + f"Dealing card to {player_name}: {card}" + Style.RESET_ALL, end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print("\n")

def main():
    """
    Main function to run the Texas Hold'em game.
    """
    table = Table()
    players = create_players()
    
    shuffle_animation()
    table.shuffle_package()
    
    for player in players:
        for _ in range(2):  # Assuming each player gets 2 cards
            card = table.draw_card()
            deal_card_animation(player.name, card)
            player.add_card(card)
    
    for round_name in ["Flop", "Turn", "River"]:
        clear_terminal()
        print(Fore.GREEN + f"\n*** {round_name.upper()} ***\n" + Style.RESET_ALL)
        table.distribute_common_cards(3 if round_name == "Flop" else 1)
        display_table(table)
        if table.betting_round(players):
            return  # End the game if only one player is active
    
    # Final evaluation
    clear_terminal()
    evaluator = Evaluator()
    best_hand = None
    winner = None
    
    suit_map = {'Hearts': 'h', 'Diamonds': 'd', 'Clubs': 'c', 'Spades': 's'}
    rank_map = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': 'T', 'J': 'J', 'Q': 'Q', 'K': 'K', 'A': 'A'}
    
    print(Fore.GREEN + "\nFinal Results:\n" + Style.RESET_ALL)
    for player in players:
        player_hand = [Card.new(rank_map[card.value] + suit_map[card.suit]) for card in player.cards]
        common_hand = [Card.new(rank_map[card.value] + suit_map[card.suit]) for card in table.common_cards]
        score = evaluator.evaluate(common_hand, player_hand)
        hand_class = evaluator.get_rank_class(score)
        hand_name = evaluator.class_to_string(hand_class)
        print(f"{player.name} ({display_card(player.cards)}): Score {score} ({hand_name})")
        if best_hand is None or score < best_hand:
            best_hand = score
            winner = player
    
    print(Fore.RED + f"\nThe winner is {winner.name} with a score of {best_hand}!\n" + Style.RESET_ALL)

def create_players():
    """
    Creates and initializes players for the game.

    Returns:
        list: A list of Player objects.
    """
    players = []
    while True:
        try:
            num_players = int(input("Enter the number of players (minimum 2, maximum 10): "))
            if num_players < 2 or num_players > 10:
                raise ValueError("Invalid number of players.")
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number between 2 and 10." + Style.RESET_ALL)
    
    for i in range(num_players):
        name = input(f"Enter the name for player {i+1}: ")
        while True:
            try:
                chips = int(input(f"Enter the number of chips for {name} (e.g., 100, 200, 500): "))
                break
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a valid number of chips." + Style.RESET_ALL)
        players.append(Player(name, chips))
    
    return players

if __name__ == "__main__":
    main()