import random


# I imported random because I want the computer to
# randomly choose a number instead of me deciding it.
def guess():

    # I generate a random number between 1 and 10.
    # This becomes the number the player has to guess.
    secret_number = random.randint(1, 10)

    # I don't want the player to keep guessing forever,
    # so I decided to give them a maximum of 5 attempts.
    max_attempts = 5

    # I use a for loop because I already know exactly
    # how many times the player is allowed to try.
    for attempts in range(max_attempts):

        try:

            # input() gives me a string, so I convert it to an
            # integer because I need to compare it with a number.
            user_guess = int(input("Enter your guess : "))

            # First, I check if the player guessed the number correctly.
            # If they did, there is no reason to continue the loop.
            if user_guess == secret_number:

                print("Congrats \nYou guessed right")

                # break stops the loop immediately because
                # the player has already won.
                break

            # If the guess is smaller than the secret number,
            # I tell the player that their guess was too low.
            elif user_guess < secret_number:

                print("Your guess is too low")

            # If the guess isn't equal to or smaller than the
            # secret number, it must be greater than it.
            else:

                print("Your guess is too high")

        # The player might type something like "hello" instead
        # of a number. int() cannot convert that into an integer,
        # so Python raises a ValueError.
        except ValueError:

            # Instead of crashing the whole program, I tell the
            # user what went wrong and let them try again.
            print("Value Error. Please enter a valid number")

            # I use continue because an invalid input should not
            # execute the rest of the current loop iteration.
            continue

    # This else belongs to the FOR loop.
    # It runs only when all 5 attempts are used without
    # the player correctly guessing the number.
    else:

        print("Better luck next time!!!")

        # Since the player failed all their attempts,
        # I reveal the correct number to them.
        print(f"The correct number was {secret_number}")


# I call the function here so that the guessing game actually starts.
guess()
