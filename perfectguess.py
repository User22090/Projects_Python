# Program to make a perfect guess
import random
import os
def clean():
    input("Press Enter to clear....")
    clear()
def clear():
    os.system("cls")
def goodbye():
    print(
    "\n\033[36m====================================\033[0m\n"
    "\033[32m      🎮 Thanks for playing!! 🎮\033[0m\n"
    "\033[33m         See you next time!\033[0m\n"
    "\033[36m====================================\033[0m"
    )
    clean()
def end():
    clear()
    print(f"The correct number was {num}")
    goodbye()
    exit()
clear()
def restart():
    clear()
    print(
        "\n\033[36m=====================================================\033[0m\n"
        "\033[33m              Do you want to restart?\033[0m\n\n"
        "\033[32m                 Yes → Restart\033[0m\n"
        "\033[31m                 No  → Quit\033[0m\n"
        "\033[36m=====================================================\033[0m"
        )
def invalid():
    clear()
    print("\n\033[31m❌ Invalid Choice!\033[0m")
def difficulty():
    while(True):
        lvl = input('''Enter difficulty level:
                   \033[32mEasy\033[0m
                   \033[33mMedium\033[0m
                   \033[31mHard\033[0m
Choice: ''')
        if lvl.lower() == "easy":
            return random.randint(1,100)
        elif lvl.lower() == "medium":
            return random.randint(1,200)
        elif lvl.lower() == "hard":
            return random.randint(1,300)
        else:
            invalid()
            restart()
            choice = input("Choice: ").strip().title()
            if choice == "Yes":
                continue
            elif choice == "No":
                clear()
                goodbye()
                exit()
            else:
                invalid()
                input("\nPress Enter to continue...")
                continue
guesses = 0
n = -1
print(
    "\033[36m=====================================================\033[0m\n"
    "\033[37m                     HELLO!                          \033[0m\n"
    "\033[36m=====================================================\033[0m\n"
    "\033[35m          Welcome to \"The Guess Game\"          \033[0m\n\n"
    "\033[37m          \033[36mType\033[0m \033[33m'End'\033[37m \033[36manytime to quit\033[0m\n"
    "\033[36m=====================================================\033[0m"
    )
num = difficulty()
clear()
while( n!= num):
    guesses += 1
    n = input("\033[34mEnter your guess: \033[0m").title()
    if n == "End":
        end()
    try:
        n = int(n)
    except ValueError:
        invalid()
        guesses -= 1
        restart()
        while True:
            choice = input("Choice: ").strip().title()
            if choice == "Yes":
                clear()
                break
            elif choice == "No":
                goodbye()
                exit()
            else:
                invalid()
        continue
    if n>num:
        print("Enter a smaller number")
        continue
    elif n<num:
        print("Enter a larger number")
        continue
os.system("cls")
print(f"\033[32mYay! You are absolutely correct\nYou took \033[31m{guesses}\033[0m \033[32mguesses to reach the right number, {num}\033[0m")
goodbye()
