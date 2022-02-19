''' Game Name: Snake-Water-Gun Game
Instructions:
1.In this game computer choose random one, you can choose your wish
2.The winning based on game rules
--> if two of you choose same one, the game is tie
--> snake vs gun = gun wins
--> gun vs water = water wins
--> water vs snake = snake wins'''
import random
def gameWin(computer,you):
	if computer==you:
		return None
	elif computer=='s':
		if you=='w':
			return False
		elif you=='g':
			return True
	elif computer=='w':
		if you=='g':
			return False
		elif you=='s':
			return True
	elif computer=='g':
		if you=='s':
			return False
		elif you=='w':
			return True

computer=print("Computer Turn: snake(s) or water(w) or gun(g)?\n")
randNo=random.randint(1,3)
if randNo==1:
	computer='s'
elif randNo==2:
	computer='w'
elif randNo==3:
	computer='g'
you=input("Your Turn: snake(s) or water(w) or gun(g)?\n")
a=gameWin(computer,you)
print(f"Computer chose: {computer}")
print(f"You chose: {you}")
if a==None:
	print(" The game is tie!")
elif a==True:
	print("Congradulations! You win the game! Great play this time!")
else:
	print("Sorry,You lose the game this time! Better luck next time!")



























