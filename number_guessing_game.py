import random

def get_valid_number(min_val, max_val):
    while True:
        try:
            num = int(input(f"Enter a number ({min_val} - {max_val}): "))
            if min_val <= num <= max_val:
                return num
            else:
                print("Out of range!")
        except ValueError:
            print("Invalid input! Numbers only.")

def choose_difficulty():
    print("\nChoose Difficulty")
    print("1. Easy   (1 - 50, 10 attempts)")
    print("2. Medium (1 - 100, 7 attempts)")
    print("3. Hard   (1 - 200, 5 attempts)")

    while True:
        choice = input("Select (1/2/3): ")
        if choice == '1':
            return 1, 50, 10
        elif choice == '2':
            return 1, 100, 7
        elif choice == '3':
            return 1, 200, 5
        else:
            print("Invalid choice!")

def play_game():
    start, end, max_attempts = choose_difficulty()
    answer = random.randint(start, end)

    attempts = 0
    previous_diff = None

    print("\nGame Started!")

    while attempts < max_attempts:
        guess = get_valid_number(start, end)
        attempts += 1

        diff = abs(answer - guess)

        if guess == answer:
            print(f"\n🎉 Correct! The answer is {answer}")
            print(f"🏆 Attempts used: {attempts}/{max_attempts}")
            return

        # Hint system (warmer / colder)
        if previous_diff is not None:
            if diff < previous_diff:
                print("🔥 Warmer!")
            else:
                print("❄️ Colder!")

        previous_diff = diff

        if guess < answer:
            print("Try bigger!")
        else:
            print("Try smaller!")

        print(f"Attempts left: {max_attempts - attempts}")

    print(f"\n💀 Game Over! The correct answer was {answer}")

# -------- MAIN LOOP --------
print("========== 🎲 ADVANCED NUMBER GUESSING GAME 🎲 ==========")

while True:
    play_game()
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
