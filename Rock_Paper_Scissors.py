import random

user_moves = {"Rock": 0, "Paper": 1, "Scissors": 2}
computer_moves = {0: "Rock", 1: "Paper", 2: "Scissors"}


def generate_computer_moves():
    r = random.randint(0, 2)

    return r


def generate_user_moves():
    answer = input("Enter the move: ")

    answer_value = user_moves[answer]

    return answer_value


def judge(user, computer):

    user_score = 0
    computer_score = 0

    if user == computer:
        print("Tie")
    elif user > computer:
        print("You win!")
        user_score += 1
    elif user < computer:
        print("Computer win!")
        computer_score += 1
    return user_score, computer_score


while True:
    user_turn = generate_user_moves()

    computer_turn = generate_computer_moves()

    print(user_turn, "\n", computer_turn)
    print(judge(user_turn, computer_turn))
