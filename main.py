import random

random_num = random.randint(1, 100)

cart = []
cart.append(random_num)
guesses = 0

while True:
    choice = int(input("Enter your random number: "))
    if choice == random_num:
        print()
        print("---------------------------")
        print("Your guess is right!")
        print("---------------------------")
        break
    elif choice > random_num:
        print("You guess is greater than random number.")
        guesses += 1
    elif choice < random_num:
        print("You guess is less than random number.")
        guesses += 1
    else:
        print("Sorry, wrong guess.Try again!")

print()
print(f"Random number was: {random_num}")
print(f"You guessed {guesses} times.")