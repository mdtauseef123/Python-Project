import random
import art
import os
def deal_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)
def calculate_score(cards):
	score=sum(cards)
	if 11 in cards and 10 in cards and score==21:
		return 0
	if 11 in cards and score>21:
		cards.remove(11)
		cards.append(1)
		score=sum(cards)
	return score
def compare(userScore,computerScore):
	if user_score > 21 and computer_score > 21:
		return "You Loose"
    if user_score == computer_score:
    	return "Draw 🙃"
    elif computer_score == 0:
    	return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
    	return "Win with a Blackjack 😎"
    elif user_score > 21:
    	return "You went over. You lose 😭"
    elif computer_score > 21:
    	return "Opponent went over. You win 😁"
    elif user_score > computer_score:
    	return "You win 😃"
    else:
    	return "You lose 😤"
def playGame():
	print(art.logo)
	user_cards=[]
	computer_cards=[]
	isGameOver=False
	for _ in range(2):
		user_cards.append(deal_card())
		computer_cards.append(deal_card())
	userScore=calculate_score(user_cards)	
	computerScore=calculate_score(computer_cards)
	print(f"\tYour cards: {userCard}, current score: {calculateScore(userCard)}")
	print(f"\tComputer's first card: {computerCard[0]}")
	if userScore==0 or computerScore==0 or userScore>21:
		isGameOver=True
	else:
		dealContinue=input("Type 'y' to get another card, type 'n' to pass: ")
		if dealContinue=="y":
			user_cards.append(deal_card())
		else:
			isGameOver=True
	while computerScore!=0 and computerScore<16:
		computerCard.append(random.choice(cards))
		computerScore=calculateScore(computerCard)
	print(f"\tYour final hand: {userCard}, final score: {userScore}")
	print(f"\tComputer\'s final hand: {computerCard}, final score: {computerScore}")
	print(compare(userScore,computerScore))
	gameContinue=input("Would you like to play again? Press 'yes' for playing or Press 'no' for exit: ")
	if gameContinue=="yes":
		os.system('clear')
		playGame()
	else:
		return
print("\t\t\tWelcome To TAU Games")
playGame()
