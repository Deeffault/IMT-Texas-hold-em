from colorama import Fore, Style
from utils import SUIT_SYMBOLS

def display_card(cards):
    """
    Displays a list of cards with their suit symbols and colors.

    Args:
        cards (list): A list of Card objects.

    Returns:
        str: A string representation of the cards.
    """
    card_strings = []
    for card in cards:
        suit_symbol = SUIT_SYMBOLS[card.suit]
        color = Fore.RED if card.suit in ['Hearts', 'Diamonds'] else Fore.BLUE
        card_strings.append(f"{color}{card.value}{suit_symbol}{Style.RESET_ALL}")
    return " ".join(card_strings)

def display_table(table):
    """
    Displays the current state of the table, including common cards and blind.

    Args:
        table (Table): The Table object representing the game state.
    """
    print(Fore.YELLOW + "\n" + "=" * 50 + Style.RESET_ALL)
    print(Fore.CYAN + f"Common Cards: {display_card(table.common_cards)}" + Style.RESET_ALL)
    print(Fore.MAGENTA + f"Blind: {table.blind}" + Style.RESET_ALL)
    print(Fore.YELLOW + "=" * 50 + Style.RESET_ALL)