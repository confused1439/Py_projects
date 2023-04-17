import random

user_score = 0
computer_score = 0
computer_moves = {0: "Rock", 1: "Paper", 2: "Scissors"}

# Function to take input from user


def generate_computer_moves():
    r = random.randint(0, 2)

    return computer_moves[r]

# Function to take input from computer


def generate_user_moves():
    answer = input("Enter the move: ")
    return answer


ans = 'y'

while ans == 'y':

    user_turn = generate_user_moves()
    computer_turn = generate_computer_moves()

    print(user_turn)
    print(computer_turn)

    if user_turn == computer_turn:
        print("Tie")
        user_score += 1
        computer_score += 1
    elif user_turn == 'Paper' and computer_turn == 'Rock':
        print("You win!")
        user_score += 1
    elif user_turn == 'Rock' and computer_turn == 'Scissors':
        print("You win!")
        user_score += 1
    elif user_turn == 'Scissors' and computer_turn == 'Paper':
        print("You win!")
        user_score += 1
    elif user_turn == 'Rock' and computer_turn == 'Paper':
        print("Computer win!")
        computer_score += 1
    elif user_turn == 'Scissors' and computer_turn == 'Rock':
        print("Computer win!")
        computer_score += 1
    elif user_turn == 'Paper' and computer_turn == 'Scissors':
        print("You win!")
        computer_score += 1

    ans = input("\nDo you want to play more? (y/n) ")

print("\nYour Score:", user_score)
print("Computer Score:", computer_score)
