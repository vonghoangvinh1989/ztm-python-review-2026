# exercise guessing game
import random
import sys

smallest = int(sys.argv[1])
largest = int(sys.argv[2])

answer_number = random.randint(smallest, largest)
print(f"answer_number is: {answer_number}")
while True:
    try:
        guessing_number = int(input(f"Please enter your guess {smallest}~{largest}: "))

        if (
            guessing_number >= smallest
            and guessing_number <= largest
            and guessing_number == answer_number
        ):
            print("Your answer is correct.")
            break
        else:
            print(f"hey bozo, I said from {smallest}~{largest}")
    except Exception as error:
        print(f"error is {error}")
        continue
