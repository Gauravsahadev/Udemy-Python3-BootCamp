print("Rock..")
print("Paper..")
print("Scissor..")

player1=input("player1,make your move: ")
player2=input("player2,make your move: ")

if player1=="Rock" and player2=="Paper":
	print("player2 wins!")
elif player1=="Paper" and player2=="Scissor":
	print("player2 wins!")
elif player1=="Scissor" and player2=="Rock":
	print("player2 wins!")
elif player1=="Rock" and player2=="Scissor":
	print("player1 wins!")
elif player1=="Paper" and player2=="Rock":
	print("player1 wins!")
elif player1=="Scissor" and player2=="Paper":
	print("player1 wins!")
elif player1==player2:
	print("Game Tie!")
else:
	print("Something Wrong!")