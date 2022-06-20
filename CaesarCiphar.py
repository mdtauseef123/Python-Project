import art
print(art.logo)

#Function purely for performing encoding the string
def encrypt(text,shift):
	modText=""
	#If shift>26 then in that case we will cut down the exact shift number by getting the remainder when / by 26
	if shift>26:
		shift=shift%26
	for ch in text:
		av=ord(ch)
		av+=shift
		if av>122:
			av=96+(av-122)
		modText+=chr(av)
	print(f"Encrypted String is:- {modText}")

#Function purely for performing decoding the string
def decrypt(text,shift):
	decText=""
	if shift>26:
		shift=shift%26
	for ch in text:
		av=ord(ch)
		av-=shift
		if av<97:
			av=96+(97-av)
		decText+=chr(av)
	print(f"Decrypted String is:- {decText}")


#Function which will perform both the task according to the parameter is being passed in dir
def caesar(text,shift,dir):
	finalText=""
	if shift>26:
		shift=shift%26
	for ch in text:
		av=ord(ch)
		if ch.isalpha():
			if dir=="encode":
				av+=shift
				if av>122:
					av=96+(av-122)
			else:
				av-=shift
				if av<97:
					av=96+(97-av)
		finalText+=chr(av)
	print(f"The {dir}d String is:- {finalText}")

choice=True
while choice:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	caesar(text,shift,direction)
	ask=input("Do you want to continue?Type 'yes' if you want to go again otherwise type 'no'")
	if ask=="no":
		choice=False
print("GoodBye")
