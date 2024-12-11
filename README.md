# IMT-Texas-hold-em

pip --version

python -m pip install -r requirements.txt

Here's a suggested README file for your project:

---

# IMT Texas Hold'em Poker Game

## Description
This project is a Python-based implementation of the popular card game **Texas Hold'em Poker**, designed with an emphasis on Object-Oriented Programming (OOP). The application simulates a complete poker game, including card dealing, betting rounds, community cards (flop, turn, river), and hand evaluation.

## Features
- **Card Deck Simulation**: A standard 52-card deck is implemented with shuffling and card dealing.
- **Player Management**: Supports multiple players, with individual hand cards, chip counts, and game statuses (e.g., fold, all-in).
- **Betting System**: Implements betting, raising, and folding during each game round.
- **Game Phases**: Handles all phases of the game (Pre-flop, Flop, Turn, River).
- **Hand Evaluation**: Determines the winning hand using poker rules.
- **Extendability**: The game structure is modular, allowing for future enhancements such as AI players or graphical interfaces.

## Requirements
- Python 3.8 or higher
- Libraries: `random` (built-in), additional library `treys` (optional, for hand evaluation)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/texas-holdem-poker.git
   cd texas-holdem-poker
   ```
2. (Optional) Install the `treys` library for advanced hand evaluation:
   ```bash
   pip install treys
   ```

## Usage
1. Run the game script:
   ```bash
   python texas_holdem.py
   ```
2. Follow the on-screen prompts to play the game.

## Project Structure
```
Texas-Holdem-Poker/
│
├── texas_holdem.py        # Main game logic
├── models/
│   ├── card.py            # Card and deck implementation
│   ├── player.py          # Player class
│   ├── table.py           # Table and game management
├── utils/
│   ├── hand_evaluation.py # Hand ranking and evaluation
│
├── README.md              # Project documentation
└── requirements.txt       # List of dependencies
```

## How to Play
1. **Start the Game**: Each player is dealt two private cards.
2. **Betting Rounds**:
   - Players can fold, check, call, or raise during each betting round.
3. **Community Cards**:
   - Flop: Three cards are dealt face-up.
   - Turn: One additional card is dealt face-up.
   - River: One final card is dealt face-up.
4. **Hand Evaluation**:
   - The winner is determined by comparing the best five-card hands for each player, using their private cards and the community cards.

## Future Improvements
- Add support for AI opponents.
- Create a graphical user interface (GUI) for enhanced user experience.
- Expand the betting system with more rules (e.g., blinds, ante).
- Add multiplayer support over the network.

## Contributing
Feel free to contribute to this project by submitting a pull request or reporting an issue.