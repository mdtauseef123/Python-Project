import art
import random
import game_data
import os
print(art.logo)
datas=game_data.data
firstDataIndex=random.randint(0,len(datas)-1)
firstData=datas[firstDataIndex]
gameContinue=True
score=0
while gameContinue:
	secondDataIndex=random.randint(0,len(datas)-1)
	secondData=datas[secondDataIndex]
	#In case if both the same account is being fetched randomly
	#We will keep generating the random account until we get different account
	while firstData==secondData:
		secondDataIndex=random.randint(0,len(datas)-1)
		secondData=datas[secondDataIndex]
	print(f"Compare A: {firstData['name']}, a {firstData['description']}, from {firstData['country']}.")
	print(art.vs)
	print(f"Against B: {secondData['name']}, a {secondData['description']}, from {secondData['country']}.")
	choice=input("Who has more followers? Type 'A' or 'B': ")
	if firstData['follower_count']>secondData['follower_count']:
		ans="A"
	else:
		ans="B"
	if choice==ans:
		score+=1
		gameContinue=True
		os.system('clear')
		print(art.logo)
		print(f"You\'re right! Current score: {score}.")
		firstData=secondData
	else:
		gameContinue=False
		os.system('clear')
		print(f"Sorry, that\'s wrong. Final score: {score}")
