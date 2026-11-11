import random




def guess():

  secret_number = random.randint(1,10)
  max_attempts = 5

  for attempts in range(max_attempts):
      
      try:

        user_guess = int(input("Enter your guess :"))

        if user_guess == secret_number :

          print("congrats \n You guessed right")

          break

        elif user_guess < secret_number :

          print("Your guess is too low")

        else:
          print("Your guess is too high")

      except ValueError:
        print("Value Error. Please enter a valid number")
        continue

  else:

      print("Better luck next time!!!")
      print(f"The correct number was {secret_number}")


guess()

