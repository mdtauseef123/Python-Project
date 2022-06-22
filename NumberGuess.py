import random
import art
import os
def playGame(attempts,number):
	choose=True
	while choose and attempts!=0:
		print(f"You have {attempts} attempts remaining to guess the number.")
		guess=int(input("Make a guess: "))
		if guess>number:
			print("Too High")
			if attempts!=0:
				print("Guess Again")
			attempts-=1
		elif guess<number:
			print("Too Low.")
			if attempts!=0:
				print("Guess Again")
			attempts-=1
		elif guess==number:
			print(f"You got it! The answer was {number}")
			choose=False
	if attempts==0:
		print("You\'ve run out of guesses, you lose.")

userContinue=True
while userContinue:
	number=random.randint(1,100)
	os.system('clear')
	print(art.logo)
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
	print(f"The random number is:- {number}")
	if difficulty=="easy":
		attempts=10
	else:
		attempts=5
	playGame(attempts,number)
	choice=input("Press 'yes' for playing another game otherwise press 'no': ")
	if choice=="no":
		userContinue=False
os.system('clear')
print("\t\t\t***********Thank You for Playing The Game**********")
print("\t\t\t\t********Do share with your friend*********")
