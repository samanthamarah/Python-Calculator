#Samantha Marah
#A Simple Program That Creates A Calculator In The Python Programming Language

#Main Functions For The Calculator

#Adds Two Numbers Together And Returns The Result
def Addition(x, y):
	return x + y

#Subtracts Two Numbers From Each Other And Returns The Result
def Subtraction(x, y):
	return x - y

#Multiplies Two Numbers Together And Returns The Result
def Multiplication(x, y):
	return x * y

#Divides Two Numbers From Each Other And Returns The Result
def Division(x, y):
	return x / y

#Returns The Result Of X To The Power Of Y
def Power(x, y):
	return x ** y

#Returns The Modulo Of X And Y
def Modulus(x, y):
	return x % y

#Welcomes The User To The Calculator
def WelcomeIntroduction():
	print("Welcome To The Python Calculator")

def Calculations():
	#User Interface
	print("Please Select The Operation You'd Like To Be Carried Out")
	print("Option 1 - Addition")
	print("Option 2 - Subtraction")
	print("Option 3 - Multiplication")
	print("Option 4 - Division")
	print("Option 5 - Power")
	print("Option 6 - Modulus")

	#User Choice Input - Player Inputs A Number Between 1 - 7
	#The Keyboard Input Is Used To Decide Which Operation To Carry Out
	UserChoice = input("Please Enter A Number Between 1 - 7 To Choose The Operation You'd Like To Be Carried Out: ")

	#Takes In The First Number To Be Used In The Operation
	FirstNumber = int(input("Please Enter Your First Number: "))

	#Takes In The Second Number To Be Used In The Operation
	SecondNumber = int(input("Please Enter Your Second Number: "))

	#If The Keyboard Input Is 1
	if UserChoice == '1':
		#Then The Addition Operation Is Carried Out
		print(FirstNumber, "+", SecondNumber, "=", Addition(FirstNumber,SecondNumber))

	#If The Keyboard Input Is 2
	elif UserChoice == '2':
		#Then The Subtraction Operation Is Carried Out
		print(FirstNumber, "-", SecondNumber, "=", Subtraction(FirstNumber, SecondNumber))

	#If The Keyboard Input Is 3
	elif UserChoice == '3':
		#Then The Multiplication Operation Is Carried Out
		print(FirstNumber, "*", SecondNumber, "=", Multiplication(FirstNumber, SecondNumber))

	#If The Keyboard Input Is 4
	elif UserChoice == '4':
		#Then The Division Operation Is Carried Out
		print(FirstNumber, "/", SecondNumber, "=", Division(FirstNumber, SecondNumber))

	#If The Keyboard Input Is 5
	elif UserChoice == '5':
		#Then The Power Operation Is Carried Out
		print(FirstNumber, "**", SecondNumber, "=", Power(FirstNumber, SecondNumber))

	#If The Keyboard Input Is 6
	elif UserChoice == '6':
		#Then The Modulus Operation Is Carried Out
		print(FirstNumber, "%", SecondNumber, "=", Modulus(FirstNumber, SecondNumber))

	#If The Keyboard Input Is Not Between The Range Of 1-4
	else:
		#Then The Input Is Considered To Be Invalid
		print("Your Input Is Invalid")

	NewCalculations()

def NewCalculations():
	print("Would You Like To Carry Out A New Calculation?")
	NewCalculation = input("Enter 'Y' For YES Or 'N' For NO: ")

	if NewCalculation.upper() == 'Y':
		Calculations()

	elif NewCalculation.upper() == 'N':
		print("Goodbye")

	else:
		NewCalculation()

WelcomeIntroduction()
Calculations()