import random

print('Welcome to number guessing!')
name = input("What's your name? ")
choice_number = input("Enter the challenge ceiling number: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Error: entered value is not numeric. Please run again and enter a number")
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    user_answer = input("Guess the number: ")

    if user_answer.isdigit():
        user_answer = int(user_answer)
    else:
        print("Error: entered value is not numeric. Please enter a number!")
        continue

    n_choices = n_choices + 1
    if user_answer == random_number:
        print("Nice! {} Win with {} attempts!".format(name, n_choices))
        break
    elif user_answer > random_number:
        print("Loss! Try a lower number..")
    else:
        print("Loss! Try a higher number..")
