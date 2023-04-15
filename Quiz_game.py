print("Welcome to my Quiz game!")

playing = input("Do you want to play? ").lower()
score = 0

# Condition
if playing != 'yes':
    quit()

print("Okay! Let's play :)")

# Question 1
answer = input("What does CPU stands for? ")

if answer == 'Central Processing Unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("What does GPU stands for? ")

if answer == 'Graphic Processing Unit':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("What does RAM stands for? ")

if answer == 'Random Access Memory':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("What does PSU stands for? ")

if answer == 'Power Supply':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Print the result
print("\nYour score is: ", score, "/4")
