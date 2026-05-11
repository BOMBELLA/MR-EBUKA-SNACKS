player_1 = input("Enter a word(ROCK, PAPER OR SCISSORS: ")
player_2 = input("Enter a word(ROCK, PAPER OR SCISSORS: ")


if player_1 == "rock" and player_2 == "scissors":
     print("Player 1 wins")
elif player_1 == "rock" and player_2 == "paper":
    print("player 2 wins")

elif player_1 == "paper" and player_2 == "rock":
    print("player 2 wins")
elif player_1 == "paper" and player_2 == "scissors":
    print("player 2 wins")

elif player_1 == "scissors" and player_2 == "paper":
    print("Tie")
else:
    print("Tie")
