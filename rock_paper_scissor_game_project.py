''' Game Name: Rock-Paper-Scissor Game
Instructions:
1.In this game computer choose random one, you can choose your wish
2.The winning based on game rules
--> if you two choose same one, the game is tie
--> rock vs paper = paper wins
--> paper vs scissor = scissor wins
--> scissor vs rock = rock wins'''
import random
def gameWin(computer,you):
	if computer==you:
		return None
	elif computer=='r':
		if you=='s':
			return False
		elif you=='p':
			return True
	elif computer=='p':
		if you=='r':
			return False
		elif you=='s':
			return True
	elif computer=='s':
		if you=='p':
			return False
		elif you=='r':
			return True

computer=print("Computer Turn: rock(r) or paper(p) or scissor(s)?\n")
randNo=random.randint(1,3)
if randNo==1:
	computer='r'
elif randNo==2:
	computer='p'
elif randNo==3:
	computer='s'
you=input("Your Turn: rock(r) or paper(p) or scissor(s)?\n")
a=gameWin(computer,you)
print(f"Computer chose: {computer}")
print(f"You chose: {you}")
if a==None:
	print(" The game is tie!")
elif a==True:
	print("Congradulations! You win the game! Great play this time!")
else:
	print("Sorry,You lose the game this time! Better luck next time!")



























