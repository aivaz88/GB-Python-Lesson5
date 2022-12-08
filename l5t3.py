# Создайте программу для игры в ""Крестики-нолики"".

import random

def PrintBoard(array):
    for i in array:
        for j in i:
            print(str(j) + ' | ', end='')
        print()
        
def CheckWinner(array):
    if array[0][0] == array[0][1] == array[0][2]: return True
    elif array[1][0] == array[1][1] == array[1][2]: return True
    elif array[2][0] == array[2][1] == array[2][2]: return True
    elif array[0][0] == array[1][0] == array[2][0]: return True
    elif array[0][1] == array[1][1] == array[2][1]: return True
    elif array[0][2] == array[1][2] == array[2][2]: return True
    elif array[0][0] == array[1][1] == array[2][2]: return True
    elif array[0][2] == array[1][1] == array[2][0]: return True
    else: return False

def ChangeBoard(ch_board, x, pl):
    for i in range(len(ch_board)):
        for j in range(len(ch_board[0])):
            if ch_board[i][j] == str(x):
                ch_board[i][j] = pl
    return ch_board                

board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
player = random.randint(0, 1)
print('Крестики - Нолики')
print()
PrintBoard(board)
count = 0
while count < 9:
    if player == 0:
        x = input('Ходят нолики! Выбирай номер ячейки: ')
        board = ChangeBoard(board, x, 'O')
        PrintBoard(board)
        player = 1
    elif player == 1:
        x = input('Ходят крестики! Выбирай номер ячейки: ')
        board = ChangeBoard(board, x, 'X')
        PrintBoard(board)
        player = 0
    if CheckWinner(board): 
        break
    count += 1
if player == 1 and count != 9:
    print('Победили нолики!')
elif player == 0 and count !=9:
    print('Победили крестики!')
else:
    print('Ничья!')
        

