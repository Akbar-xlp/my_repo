"""
["rock", "paper", "scissors"]
["таш", "кагаз", "кайчы"]

Enter a choice (rock, paper, scissors):
Тандоо киргизиңиз (таш, кагаз, кайчы):

Invalid choice. Please try again.
Туура эмес тандоо. Сураныч, кайра аракет кылыңыз.

Your choice:
Сиздин тандоонуз:

Computer's choice:
Компьютердин тандоосу:
"""


def get_computer_choice():
    import random
    return random.choice(['rock', 'paper', 'scissors'])


def get_player_input():
    data = input("Enter a choice (rock, paper, scissors): ").lower()
    if data not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        return get_player_input()
    return data


def check_winner(computer, player):
    if player == computer:
        return "It's a tie!"
    if (player == 'rock' and computer == 'scissors') or \
            (player == 'scissors' and computer == 'paper') or \
            (player == 'paper' and computer == 'rock'):
        return "Winner player!"

    return "Winner computer!"


def play():
    computer = get_computer_choice()
    player = get_player_input()

    print(f"Your choice: {player}")
    print(f"Computer's choice: {computer}")

    result = check_winner(computer, player)

    print(result)


play()
