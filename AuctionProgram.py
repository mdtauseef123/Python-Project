import art
import os
print(art.logo)
print("Welcome to the secret auction program.")
repeat=True
bidders={}
while repeat:
	name=input("What is your name?: ")
	bid=int(input("What's your bid?: $"))
	bidders[name]=bid
	choice=input("Are there any other bidders? Type 'yes' or 'no'.")
	if choice=="yes":
		repeat=True
	else:
		repeat=False
	os.system('clear')
bno=0
bname=""

for x,y in bidders.items():
	if y>bno:
		bno=y
		bname=x
print(f"The winner is {bname} with a bid of ${bno}")
