#------------------ METADATA -------------------
# NAME: Alexei Luchian
# USERNAME: f24alelu
# COURSE: Script Programming IT384G - Spring 2025
# ASSIGNMENT: Assignment 1 - Python - Task 3
# DATE OF LAST CHANGE: 2025-05-01
#-----------------------------------------------

import random

'''the function responsible for reading the highscore, arranging the players and outputting the table and overwriting the
data in the file'''


def check_highscore(username, guesses):
    players = []
    highscores = []

    # Step 1: Read the highscore file
    try:
        with open("highscore.csv") as hs:
            for score in hs:
                score = score.strip('\n')
                score = score.split(';')
                players.append(score[0])
                highscores.append(int(score[1]))

            if not players:
                raise FileNotFoundError
    except FileNotFoundError:
        # If file is missing, create it with default values
        with open("highscore.csv", "w") as hs:
            for _ in range(10):
                hs.write("---;1000\n")
        # Initialize with default players and scores
        players = ["---"] * 10
        highscores = [1000] * 10

    # Step 2: Insert the new score into the correct position
    if int(guesses) > highscores[-1]:
        print(f"You needed {guesses} guesses. Not enough to enter the top 10.")
    else:
        print(f"You needed {guesses} guesses. You entered the highscore list.")
        for i in range(len(highscores)):
            if int(guesses) < highscores[i]:
                highscores.insert(i, guesses)
                players.insert(i, username)
                break

    # Step 3: Slice to only keep the top 10
    players = players[:10]
    highscores = highscores[:10]

    # Step 4: Print the leaderboard
    for i in range(len(highscores)):
        if players[i] in users:
            if players[i] == username:
                print(f"| {users[players[i]]} | {highscores[i]} guesses | < YOU")
            else:
                print(f"| {users[players[i]]} | {highscores[i]} guesses |")
        else:
            if players[i] == username:
                print(f"| {players[i]} | {highscores[i]} guesses | < YOU")
            else:
                print(f"| {players[i]} | {highscores[i]} guesses |")

    # Step 5: Save the updated leaderboard back to the file
    lines = []
    for i in range(len(players)):
        lines.append(f"{players[i]};{highscores[i]}\n")
    with open("highscore.csv", "w") as final:
        final.writelines(lines)


''' the function that keeps the game going until the user quits or is out of attempts. This function also implements all
 the requirements needed for the mandatory task'''
def start_game(username):
    print(f"Hello {username}, welcome to this guessing game!")
    print("I will determine a random number between 0 and 1000 and you have to guess it.")
    print("You can quit at any time by entering 'Q'.")
    game_on = True
    number = random.randint(0, 1000)
    print(number)
    numbers = set()
    guesses = 0
    quit_flag = 0
    while game_on:
        user_input = input("Choose a number between 0 and 1000 or 'Q': ")
        if user_input == 'Q' or user_input == 'q':
            print('You quit')
            quit_flag = 1
            game_on = False
        elif user_input.isdigit():
            user_input = int(user_input)
            if 0 <= user_input <= 1000:
                if user_input == number:
                    print("This is the correct number. Congrats!")
                    game_on = False
                elif user_input > number:
                    print("PFOOOO, too big. Try again.")
                else:
                    print("meh... too small. Try again.")
                numbers.add(user_input)
                guesses += 1
            else:
                print("This doesn't look like a number between 0 and 1000, or 'Q'")
        else:
            print("This doesn't look like a number between 0 and 1000, or 'Q'")
    sorted_numbers = sorted(numbers)
    print("The unique numbers you have entered are:", ', '.join(str(num) for num in sorted_numbers))
    if not quit_flag:
        check_highscore(username, guesses)
    print("Have a nice day!")

# open and read users' data from the file
users = {}
with open("users.csv") as file:
    for line in file:
        user = line.strip('\n')
        user = user.split(';')
        users[user[0]] = user[1]

login = input("Hello, what is your login: ")
if login in users:
    start_game(users[login])
else:
    start_game(login)

# Even more code here
# I don't think so professor, I will implement everything above 😉
