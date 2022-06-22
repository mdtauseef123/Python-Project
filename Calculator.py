import art
import os
print(art.logo)
def add(a,b):
	return a+b
def subtract(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	return a/b
operations={
	"+":add,
	"-":subtract,
	"*":multiply,
	"/":divide,
}
def calculate():
	num1=float(input("Enter the first number:- "))
	print("Which operations would you like to perform?")
	for x in operations:
		print(x)
	operation_symbol=input("Enter the operation from the above line:- ")
	num2=float(input("Enter the second number:- "))
	function=operations[operation_symbol]
	res=function(num1,num2)
	print(f"{num1} {operation_symbol} {num2} = {res}")
	return res
def another_calc(num):
	operation_symbol=input("Enter the operation:- ")
	num3=float(input("Enter the next number:- "))
	function=operations[operation_symbol]
	res=function(num,num3)
	print(f"{num} {operation_symbol} {num3} = {res}")
	return res	
counter=True
val=calculate()
while counter:
	choice=input(f"Type 'y' to calculate with {val}, or type 'r' to start a new calculation or type 'n' to exit.: ")
	if choice=="y":
		val=another_calc(val)
	elif choice=="r":
		os.system('clear')
		print(art.logo)
		val=calculate()
	elif choice=="n":
		counter=False
print("Exit")
	
