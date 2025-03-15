# Blackjack Game

A simple text-based Blackjack game implemented in Python.

## Game Rules

- The goal is to get a hand value as close to 21 as possible without going over.
- Number cards (2-10) are worth their face value.
- Face cards (Jack, Queen, King) are worth 10 points.
- Aces can be worth either 1 or 11 points, whichever is more beneficial.
- The dealer must hit until they have at least 17 points.
- If you go over 21, you "bust" and lose the game.
- If the dealer busts, you win.
- If neither busts, the one with the higher hand value wins.
- If both have the same value, it's a "push" (tie).
- **Double Down**: You can choose to double down on your initial two cards. This means you'll take exactly one more card and then automatically stand. In a real casino, this would double your bet.

## How to Play

1. Run the game by executing:
   ```
   python blackjack.py
   ```
   or
   ```
   python3 blackjack.py
   ```

2. You'll be dealt two cards, and the dealer will have two cards (one face up, one face down).

3. On your turn, you can choose to:
   - **Hit (H)**: Take another card
   - **Stand (S)**: End your turn and let the dealer play
   - **Double Down (D)**: Take exactly one more card and then stand (only available on your initial two cards)

4. After each game, you'll be asked if you want to play again.

## Requirements

- Python 3.6 or higher

Enjoy the game! 