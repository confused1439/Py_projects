import random

rand_num = random.randint(0, 10)
guessed_count = 0

while True:
    guessed_count += 1

    guessed_num = int(input("Enter the guess: "))

    if guessed_num < rand_num:
        print("You are above the answer.")
        decision = input("Do you want to quit? (y/n)")

        if decision == 'y':
            print("The answer is ", rand_num)
            quit()
    elif guessed_num == rand_num:
        print("You got it!")
        break
    elif guessed_num > rand_num:
        print("You are below the answer.")
        decision = input("Do you want to quit? (y/n)")

        if decision == 'y':
            print("The answer is ", rand_num)
            quit()
    else:
        continue

print("\nYou used", guessed_count, "guess/guesses to get correct answer.")

# -------End of the code-------
