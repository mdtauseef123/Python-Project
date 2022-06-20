import random
import hangman_art
import hangman_words
print("\t\tWelcome to Hangman Game")
print(hangman_art.logo)
stages=hangman_art.stages


arr = hangman_words.word_list
index=random.randint(0,len(arr)-1)
chosen_word = arr[index]
print(f"Word is {chosen_word}")
display=[]
for i in range(0,len(chosen_word)):
	display.append("_")
print("Word Format:-")
print(''.join(display))
ctr=0
lives=6
prev=""
while ctr!=len(chosen_word) and lives!=-1:
	guess=input("Guess a letter: ").lower()
	#If the correct guess is repeated then only we will throw the message and doesn't count it
	if prev==guess:
		print(f"You have already guessed {guess}")
		continue
	else:
		prev=guess
	if not guess in chosen_word:
		print("Wrong Guess")
		print(stages[lives])
		lives-=1
		if lives!=-1:
			print(f"{lives} Lives remaining")
	else:
		for j in range(0,len(chosen_word)):
			if guess==chosen_word[j]:
				ctr+=1
				display[j]=guess
		ans=''.join(display)
		print(ans)
if ctr!=len(chosen_word):
	print("You Loose")
else:
	print("You Win")
