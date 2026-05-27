# Program for a simple Rock, Paper and Scissors game
import os
import random
def game(user,computer):
    if user == computer:
        return 0
    if user == "Rock" and computer == "Paper":
        return -1
    elif user == "Paper" and computer == "Scissors":
        return -1
    elif user == "Scissors" and computer == "Rock":
        return -1
    else:
        return 1
def goodbye():
    print(
    "\n\033[36m====================================\033[0m\n"
    "\033[32m      🎮 Thanks for playing!! 🎮\033[0m\n"
    "\033[33m         See you next time!\033[0m\n"
    "\033[36m====================================\033[0m"
    )
def restart():
    print(
        "\n\033[36m=====================================================\033[0m\n"
        "\033[33m              Do you want to restart?\033[0m\n\n"
        "\033[32m                 Yes → Restart\033[0m\n"
        "\033[31m                 No  → Quit\033[0m\n"
        "\033[36m=====================================================\033[0m"
        )
def invalid():
    print("\n\033[31m❌ Invalid Choice!\033[0m")
while True:
    os.system("cls")
    computer = random.choice(["Rock","Paper","Scissors"])
    print(
    "\033[36m=====================================================\033[0m\n"
    "\033[37m                     HELLO!                          \033[0m\n"
    "\033[36m=====================================================\033[0m\n"
    "\033[35m          Welcome to Rock, Paper & Scissors          \033[0m\n\n"
    "\033[33m                    GAME RULES\033[0m\n"
    "\033[31m                      • Rock\033[0m\n"
    "\033[32m                      • Paper\033[0m\n"
    "\033[34m                      • Scissors\033[0m\n\n"
    "\033[37m           Type \033[33m'End'\033[37m anytime to quit\033[0m\n"
    "\033[36m=====================================================\033[0m"
    )
    print("\n\033[35m► Enter your choice:\033[0m ", end="")
    user = input().lower().strip().title()
    l = ["Rock", "Paper", "Scissors"]
    if user == "End":
        goodbye()
        break
    if user not in l:
        invalid()
        restart()
        choice = input("Choice: ").strip().title()
        if choice == "Yes":
            continue
        elif choice == "No":
            goodbye()
            break
        else:
            invalid()
            input("\nPress Enter to continue...")
            continue
    result = game(user, computer)
    print(
    "\n\033[36m=====================================================\033[0m\n"
    "\033[33m                    ROUND RESULT                     \033[0m\n"
    "\033[36m=====================================================\033[0m\n"
    f"\033[35m   Your Choice      : \033[32m{user}\033[0m\n"
    f"\033[35m   Computer Choice  : \033[31m{computer}\033[0m\n"
    "\n\033[36m=====================================================\033[0m"
    )
    if result == 0:
        print("\n\033[33m⚖ The game is drawn!\033[0m")
    elif result == 1:
        print("\n\033[32m🏆 You won the game!!! Congratulations!!\033[0m")
    else:
        print("\n\033[31m💀 Better Luck Next Time!\033[0m")
    print(
    "\n\033[36m=====================================================\033[0m\n"
    "\033[33m              Do you wish to continue?\033[0m\n\n"
    "\033[32m                 Yes  → Continue\033[0m\n"
    "\033[31m                 No   → Quit\033[0m\n"
    "\033[36m=====================================================\033[0m"
    )
    choice = input().title().strip()
    if choice == "Yes":
        os.system("cls")
    elif choice == "No":
        goodbye()
        exit()
    else:
       invalid()
       input("\nPress Enter to continue...")
       continue