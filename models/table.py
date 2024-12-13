import random
from models import Card
from utils.display import display_card

class Table:
    """
    Represents the poker table and manages the game state.
    """
    def __init__(self):
        """
        Initializes a Table object.
        """
        self.common_cards = []
        self.blind = 0
        self.package = self.create_package()

    def create_package(self):
        """
        Creates a standard 52-card deck.

        Returns:
            list: A list of Card objects representing the deck.
        """
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        return [Card(value, suit) for value in values for suit in suits]

    def shuffle_package(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self.package)
        
    def distribute_cards(self, player, number=2):
        """
        Distributes a specified number of cards to a player.

        Args:
            player (Player): The player to receive the cards.
            number (int): The number of cards to distribute.
        """
        for _ in range(number):
            player.cards.append(self.package.pop())

    def draw_card(self):
        """
        Draws a card from the deck.

        Returns:
            Card: The drawn card.
        """
        return self.package.pop()

    def distribute_common_cards(self, number):
        """
        Distributes a specified number of common cards to the table.

        Args:
            number (int): The number of common cards to distribute.
        """
        for _ in range(number):
            self.common_cards.append(self.package.pop())

    def betting_round(self, players):
        """
        Conducts a betting round for the active players.

        Args:
            players (list): A list of Player objects.

        Returns:
            bool: True if the round should end, False otherwise.
        """
        active_players = [player for player in players if player.active]
        if len(active_players) == 0:
            print("All players have folded or been eliminated. No winner for this round.")
            return True  # End the round
        
        if len(active_players) == 1:
            winner = active_players[0]
            print(f"{winner.name} wins the round as the last active player!")
            winner.chips += self.blind
            self.blind = 0
            return True  # End the round

        for player in active_players:
            if player.is_eliminated():
                player.fold()
                continue

            while True:
                print(f"{player.name}, your cards: {display_card(player.cards)}")
                action = input(f"{player.name}, enter your action (bet/fold): ").strip().lower()
                if action == "fold":
                    player.fold()
                    active_players = [p for p in players if p.active]
                    if len(active_players) == 1:
                        winner = active_players[0]
                        print(f"{winner.name} wins the round as the last active player!")
                        winner.chips += self.blind
                        self.blind = 0
                        return True  # End the round
                    break
                elif action == "bet":
                    try:
                        bet_amount = int(input(f"Enter your bet amount (current chips: {player.chips}): "))
                        player.bet(bet_amount, self)
                        break
                    except ValueError as e:
                        print(f"Invalid bet: {e}")
                else:
                    print("Invalid action. Please enter 'bet' or 'fold'.")

        return False  # Continue the game


    
    def update_blind(self, amount):
        """
        Updates the blind with given amount.

        Args:
            amount (int): The amount to add to the blind.
        """
        self.blind += amount
        
    def check_winner(self, players):
        """
        Check if there is only one player left with chips or if everyone is all-in.
        """
        active_players = [player for player in players if player.chips > 0]
        
        # Si un seul joueur a des jetons, il gagne la partie
        if len(active_players) == 1:
            return active_players[0]
        
        # Si tous les joueurs sont all-in, le jeu doit continuer jusqu'au showdown
        if all(player.chips == 0 for player in players):
            print("All players are all-in. Proceeding to final evaluation.")
            return None  # Pas encore de gagnant, évaluation finale nécessaire
        
        return None