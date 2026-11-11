# Number Guessing Game 🎯

A simple command-line number guessing game built with Python.

The computer randomly selects a number between **1 and 10**, and the player gets **5 attempts** to guess it.

## Features

- Generates a random number using Python's `random` module
- Allows up to 5 guessing attempts
- Gives feedback when the guess is too high or too low
- Stops the game when the correct number is guessed
- Handles invalid input using `try-except`
- Displays the correct number if all attempts are unsuccessful

## How It Works

1. The program generates a random number between 1 and 10.
2. The player is given 5 attempts.
3. The player enters a guess.
4. The program checks the guess:
   - If it is correct, the player wins.
   - If it is too low, the program tells the player.
   - If it is too high, the program tells the player.
5. If the player uses all 5 attempts without guessing correctly, the correct number is displayed.
6. Invalid non-numeric input is handled using `ValueError`.

## Concepts Practiced

This project helped me practice:

- Variables
- Functions
- User input
- Type conversion
- `if`, `elif`, and `else`
- `for` loops
- `break`
- `continue`
- `try-except`
- `ValueError`
- `for-else`
- Python's `random` module

## Example

```text
Enter your guess: 3
Your guess is too low

Enter your guess: 8
Your guess is too high

Enter your guess: 5
Congrats!
You guessed right
```

If all attempts are used:

```text
Better luck next time!!!
The correct number was 7
```

## How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project:

```bash
cd number-guessing-game
```

Run the program:

```bash
python guessing_game.py
```

## Future Improvements

Possible improvements I can add later:

- Add a **Play Again** option
- Allow the player to choose the difficulty
- Add different number ranges
- Display the number of attempts used
- Prevent invalid input from consuming an attempt
- Keep track of the player's score
- Add automated tests

## What I Learned

This project helped me understand how different Python concepts work together.

In particular, I learned how `break` can stop a loop when the correct answer is found, how `continue` can skip an iteration after invalid input, and how `for-else` can be used to detect when a loop finishes without encountering a `break`.
