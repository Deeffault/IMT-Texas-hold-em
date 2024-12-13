from utils.display import display_card

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
    
    def bet(self, amount, table):
        """
        Places a bet by the player and updates the table blind.

        Args:
            amount (int): The amount to bet.
            table (Table): The table object to update the blind.

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
        table.update_blind(amount)
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
        
    def reset(self):
        """
        Resets the player's hand and active status for a new round
        """
        self.cards = []
        self.active = True

    def betting_round(self, players):
        """
        Conducts a betting round for the active players.

        Args:
            players (list): A list of Player objects.

        Returns:
            bool: True if the game should end, False otherwise.
        """
        active_players = [player for player in players if player.active]
        if len(active_players) <= 1:
            return True  # End the game if only one player is active

        for player in active_players:
            if player.is_eliminated():
                player.fold()
                continue

            while True:
                print(f"{player.name}, your cards: {display_card(player.cards)}")
                action = input(f"{player.name}, enter your action (bet/fold): ").strip().lower()
                if action == "fold":
                    player.fold()
                    if len([p for p in players if p.active]) == 1:
                        winner = next(p for p in players if p.active)
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