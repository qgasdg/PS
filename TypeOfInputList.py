import sys

n, m = map(int, [4, 5])
board = [list('00110'), list('00011'), list('11111'), list('00000')]

print(board)
print(type(board[0][0]))
for i in range(4):
    board[i] = list(map(int, board[i]))
print(board)
print(type(board[0][0]))
