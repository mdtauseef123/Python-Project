import art
import random
import os
print(art.logo)
print("\t\t\tWelcome To Tau Games")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def calculateScore(cardsValue):
	score=0
	for x in cardsValue:
		score+=x
	return score
shouldContinue=True
while shouldContinue:
	userCard=[]
	computerCard=[]	
	userCard.append(random.choice(cards))
	userCard.append(random.choice(cards))
	computerCard.append(random.choice(cards))
	computerCard.append(random.choice(cards))
	print(f"\tYour cards: {userCard}, current score: {calculateScore(userCard)}")
	print(f"\tComputer's first card: {computerCard[0]}")
	choice=input("Type 'y' to get another card, type 'n' to pass: ")
	if choice=="y":
		userScore=calculateScore(userCard)
		if userScore<21:
			userCard.append(random.choice(cards))
			userScore=calculateScore(userCard)
		computerScore=calculateScore(computerCard)
		print(f"\tYour cards: {userCard}, current score: {userScore}")
		print(f"\tComputer\'s first card: {computerCard[0]}")
		print(f"\tYour final hand: {userCard}, final score: {userScore}")
		print(f"\tComputer\'s final hand: {computerCard}, final score: {computerScore}")
		if userScore>21:
			print("You Loose.Computer Win")
		elif computerScore>21:
			print("You Win.Computer Loose")
		elif userScore>computerScore:
			print("You Win.Computer Loose")
		elif userScore<computerScore:
			print("You Loose.Computer Win")
		elif userScore==computerScore:
			print("Match Drawn")
	elif choice == "n":
		userScore=calculateScore(userCard)
		computerScore=calculateScore(computerCard)
		while computerScore<16:
			computerCard.append(random.choice(cards))
			computerScore=calculateScore(computerCard)
		print(f"\tYour cards: {userCard}, current score: {userScore}")
		print(f"\tComputer\'s first card: {computerCard[0]}")
		print(f"\tYour final hand: {userCard}, final score: {userScore}")
		print(f"\tComputer\'s final hand: {computerCard}, final score: {computerScore}")
		if computerScore>21:
			print("You Win.Computer Loose")
		elif userScore>21:
			print("You Loose.Computer Win")
		elif userScore>computerScore:
			print("You Win.Computer Loose")
		elif userScore<computerScore:
			print("You Loose.Computer Win")
		elif userScore==computerScore:
			print("Match Drawn")
	askAgain=input("Would you like to play again? Press 'yes' for playing or Press 'no' for exit: ")
	if askAgain=="no":
		shouldContinue=False
	else:
		shouldContinue=True
		os.system('clear')
print("\n\t\tThank You For Using This Game")
print("\t\t\tDo share with your friend")
