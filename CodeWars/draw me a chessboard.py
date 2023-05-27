# def chessBoard(columen, row):
#     board = []
#     for i in range(columen):
#         a = []
#         for j in range(row):
#             if i % 2 == 0:
#                 if j % 2 == 0:
#                     a.append('O')
#                 else:
#                     a.append('X')
#             elif i % 2 != 0:
#                 if j % 2 == 0:
#                     a.append('X')
#                 else:
#                     a.append('O')
#         board.append(a)
#     return board
#
#
# chessBoard(3, 7)

def chess_board(rows, columns):
    ans=[]
    for i in range(1,rows+1,1):
        l=[]
        for j in range(i,columns+i,1):
            if j%2!=0:
                l.append('O')
            else:
                l.append('X')
        ans.append(l)
    return ans
