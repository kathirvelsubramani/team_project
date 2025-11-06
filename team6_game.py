import random

def guess_number():
    num = random.randint(1, 10)
    guess = int(input("Guess a number (1-10): "))
    if guess == num:
        print("🎉 Correct!")
    else:
        print(f"❌ Wrong! The number was {num}.")
