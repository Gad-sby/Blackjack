# Practice Blackjack Game

A simple Blackjack game built in Python for learning and practicing programming concepts such as object-oriented programming, game logic, user input handling, and randomization.

## Features

- Deal cards from a shuffled deck
- Player can hit or stand
- Dealer follows standard Blackjack rules
- Automatic score calculation
- Ace handling (1 or 11)
- Win, lose, and push outcomes
- Command-line interface

## How to Run

### Prerequisites

- Python 3.10+ (or your version)

### Run the Game

```bash
python main.py
```

## Rules

- Goal: Get as close to 21 as possible without going over.
- Number cards count as their face value.
- Face cards (J, Q, K) count as 10.
- Aces count as 1 or 11, whichever is more beneficial.
- Dealer must hit until reaching 17 or higher.

## Example Gameplay

```text
Your hand: 10♠, 7♦ (17)
Dealer shows: K♣

Hit or Stand? h

Your hand: 10♠, 7♦, 3♥ (20)

Dealer's hand: K♣, 8♠ (18)

You win!
```

## Project Structure

```text
blackjack/
├── main.py
├── deck.py
├── card.py
├── hand.py
└── README.md
```

## Future Improvements

- Multiple decks
- Betting system
- Split hands
- Double down
- Statistics tracking
- Graphical user interface (GUI)
- Save player records

## Learning Goals

This project was created to practice:

- Python fundamentals
- Classes and objects
- Functions and modules
- Random number generation
- Game state management
- Git and GitHub workflows

## License

This project is for educational purposes.
