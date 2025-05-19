import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

symbols = ["💖", "🌟", "💘", "💫", "💍"]
credits = 10

def intro():
    clear()
    print("🎰 Welcome to Love Slots! 🎰")
    time.sleep(1.5)
    print("You start with 10 love credits 💕")
    time.sleep(1.5)
    print("Match 3 symbols to win!")
    print("Get 30 credits to unlock a special surprise... 👀")
    input("\nPress Enter to spin!")

def spin():
    return [random.choice(symbols) for _ in range(3)]

def display_slot(slot):
    print(f"| {slot[0]} | {slot[1]} | {slot[2]} |")

def check_win(slot):
    return slot.count(slot[0]) == 3

def promposal():
    clear()
    message = "💃 Will you go to prom with me? 🕺"
    border = "💘 " * ((len(message) // 2) + 2)
    print(border)
    print("💘 " + message + " 💘")
    print(border)
    print("\nType 'yes' if you will! 💖")

def game():
    global credits
    intro()
    while credits > 0:
        clear()
        print(f"Credits: {credits}")
        input("Press Enter to SPIN 🎰")
        slot = spin()
        display_slot(slot)

        if check_win(slot):
            print("✨ JACKPOT! You won 10 credits! ✨")
            credits += 10
        else:
            print("No match, try again! 💔")
            credits -= 1
        
        time.sleep(2)

        if credits >= 30:
            promposal()
            break
    else:
        clear()
        print("Aww... you're out of love credits 😢")
        print("But here's a consolation prize:")
        time.sleep(2)
        promposal()

game()

