import random


def main():
	print("Welcome to Rock, Paper, Scissors - 2017")
	runGame()

	newGame = input("Go Again? Y/N: ")
	if newGame == 'Y':
		runGame()
	else:
		pass

def runGame():
	computerChoice = computerturn()
	userChoice = input("Enter rock, paper, or scissors: ")
	print("Computer chooses " + computerChoice)

	if userChoice == computerChoice :
		print("Oh Wow! a Tie! better go again...")
		runGame()
		return

	elif userChoice == 'rock' and computerChoice == 'scissors' :
		print('Rock smashes Scissors')
		print('You Win!')
		return

	elif userChoice == 'paper' and computerChoice == 'rock' :
		print('Paper covers Rock')
		print('You Win!')
		return

	elif userChoice == 'scissors' and computerChoice == 'paper' :
		print('Scissors cuts Paper')
		print('You Win!')
		return

	elif userChoice == 'paper' and computerChoice == 'scissors' :
		print('Scissors cuts Paper')
		print('Computer Wins!')
		return

	elif userChoice == 'rock' and computerChoice == 'paper' :
		print('Paper covers Rock')
		print('Computer Wins!')
		return

	elif userChoice == 'scissors' and computerChoice == 'rock' :
		print('Rock smashes Scissors')
		print('Computer Wins!')
		return

	else:
		pass
	

def computerturn():
	choice = random.randint(1,3)
	if choice == 1:
		return 'rock'
		
	elif choice == 2:
		return 'paper'

	else :
		return 'scissors'
	




main()	