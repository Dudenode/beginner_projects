import random

wins=0
losses=0

while True:
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice (rock, paper, scissors) or 'quit' to exit:")
    user_choice = input().lower()

    if user_choice == 'quit':
        break

    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):        
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1

print(f"Final score - Wins: {wins}, Losses: {losses}")