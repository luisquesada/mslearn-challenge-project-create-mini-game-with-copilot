import random

# write the code for a game of rock, paper, scissors in the console. The game should randomly select one of the items, then get the user's selection, then determine the winner. 
# The game should keep playing until the user chooses to quit. The game should keep track of the score, and print the score after each round.
# The game should be able to handle invalid user input, and print an error message when it occurs.
def play_game():
    score = {'user': 0, 'computer': 0}

    while True:
        # Randomly select one of the items
        options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(options)

        # Get the user's selection
        user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ")

        # Check if the user wants to quit
        if user_choice.lower() == 'quit':
            break

        # Determine the winner
        if user_choice.lower() not in options:
            print("Invalid input. Please enter rock, paper, or scissors.")
            continue

        if user_choice.lower() == computer_choice:
            print("It's a tie!")
        elif (user_choice.lower() == 'rock' and computer_choice == 'scissors') or \
             (user_choice.lower() == 'paper' and computer_choice == 'rock') or \
             (user_choice.lower() == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            print(f"Computer's choice was: {computer_choice}")
            score['user'] += 1
        else:
            print("Computer wins!")
            score['computer'] += 1

        # Print the score after each round
        print(f"Score: User - {score['user']}, Computer - {score['computer']}")

    print("Thanks for playing!")

play_game()
