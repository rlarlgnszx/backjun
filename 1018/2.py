board=[]
wrong=False    
n,m = map(int,input().split())
for i in range(m):
    board.append(list(input()))

def check(i,j):
    wro=0
    if board[i][j]=="W":
        for i2 in range(i,i+8,2):
            for j2 in range(j,j+8,2):
                if board[i2][j2]!="W":
                    wro +=1                    
                if board[i2][j2+1]!="B":
                    wro +=1
                if board[i2+1][j2]!="B":
                    wro +=1
                if board[i2+1][j2+1]!="W":
                    wro +=1
    elif board[i][j]=="B":
        for i2 in range(i,i+8,2):
            for j2 in range(j,j+8,2):
                if board[i2][j2]!="B":
                    wro +=1
                if board[i2][j2+1]!="W":
                    wro +=1
                if board[i2+1][j2]!="W":
                    wro +=1
                if board[i2+1][j2+1]!="B":
                    wro +=1
    return wro
def start(board):
    for i in range(len(board)-7):
        for j in range(len(board[0])-7):
            if not wrong:
                wrong = check(i,j)
            else:
                if wrong > check(i,j):
                    wrong =check(i,j)

print(board)
start(board)



        