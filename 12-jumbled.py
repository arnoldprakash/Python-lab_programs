import random
actual_number =random.randint(0,100)
attempts = 0
while True:
    attempts += 1
    guess = int(input("Guess the number:\n"))
    if guess < actual_number:
        print("Your guess was too low")

    elif guess > actual_number:
        print("Your guess was too high")
    else:
        print(f"You guessed the number in {attempts} attempts")
        break
print("Thanks for playing with us: ")