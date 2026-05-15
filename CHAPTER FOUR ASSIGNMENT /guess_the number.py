immport random

random_number = random.randint(1, 1000):

       user = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))

while random_number != user:


       if user > random_number:
        print("Too high. Try again.")

elif user < random_number:
        print("Too low. Try again.")

user = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))

else:
       print("Congratulations. You guessed the number!")


