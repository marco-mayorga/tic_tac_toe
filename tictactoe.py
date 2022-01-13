#ask for names 
from typing import Counter


Player1 = input("Enter Player 1 name:")
Player2 = input("Enter Player 2 name:")

#ask player what symbol they want to use
symbol_choice = input(f"What symbol do you want to use {Player1}? X or O?\n").upper()



#Player1 chooses X or O and thus sets the other players sign
while True:
    if symbol_choice == "O":
        Player2_Choice = "X"
        break
    if symbol_choice == "X":
        Player2_Choice = "O"
        break
    else:
        symbol_choice = input(f"What symbol do you want to use {Player1}? X or O?\n").upper()
        break    

#Set var symbol_choice = to Player1 
Player1_Choice = symbol_choice

#list of choices.
board = []

#board lengnth
len_of_Board = len(board)

#Drawing Board
drawnBoard ="""1 | 2 | 3
- | - | -
4 | 5 | 6
- | - | -
7 | 8 | 9\n"""
NewdrawnBoard = drawnBoard

print(drawnBoard)
#Ask for player1 Input
Player1_number = int(input(f"{Player1} Choose a number on the board:"))
#setting player numbers at zero
Player2_number = 0

#Start loop
while True:
    #Player1
    if Player1_number in range(1, 9):
        Player1_number = str(Player1_number)
        board.append(Player1_number)
        NewdrawnBoard = NewdrawnBoard.replace(Player1_number , Player1_Choice)
        print(NewdrawnBoard)
        Player2_number = int(input(f"{Player2} Choose a number on the board:"))

    #Player 2 choice
    if Player2_number in range(1, 9):
        Player2_number = str(Player2_number)
        board.append(Player2_number)
        NewdrawnBoard = NewdrawnBoard.replace(Player2_number , Player2_Choice)
        print(NewdrawnBoard)
        Player1_number = int(input(f"{Player1} Choose a number on the board:"))
        print(NewdrawnBoard)

    #ends game when board is full
    if len_of_Board == int(8):
        Player1_number = str(Player1_number)
        board.append(Player1_number)
        NewdrawnBoard = NewdrawnBoard.replace(Player1_number , Player1_Choice)
        print(NewdrawnBoard)
        print("\nGame Over")
        quit()
