# sudoku solver

def findNum(s,i,j,num):
    for a in range(0,9):
        if s[i][a]==num:
            return True
    for a in range(0,9):
        if s[a][j]==num:
            return True
    for a in range(i//3*3, i//3*3+3):
        for b in range(j//3*3, j//3*3+3):
            if s[a][b]==num:
                return True
    return False

def createPossibilityCell(s,i,j):
    p=[]
    for k in range(1,10):
        if not findNum(s,i,j,k):
            p.append(k)
    return p

def findNextEmptyCell(s,i,j):
    while s[i][j]!=0:
        i+=1
        if i==9:
            j+=1
            i=0            
            if j==9:
                return (9,9)
    return (i,j)

def findCell(s,i,j):
    (i,j)=findNextEmptyCell(s,i,j)
    if j==9:
        return True
    p=createPossibilityCell(s,i,j)
    if len(p)==0:
        return False
    for v in p:
        s[i][j]=v
        finish=findCell(s,i,j)
        if finish:
            return True
    s[i][j]=0

s1=[[5,9,0,0,8,4,0,0,0],
    [0,4,0,0,0,0,0,6,9],
    [0,0,0,1,9,0,8,4,0],
    [0,0,0,2,3,6,4,5,8],
    [3,0,2,0,0,0,6,0,0],
    [0,0,0,0,0,0,3,0,0],
    [0,2,0,3,0,7,9,0,4],
    [0,3,0,0,1,0,0,0,0],
    [6,0,0,5,4,0,0,3,0]]

s2=[[4,0,0,0,0,0,0,5,8],
    [0,0,0,0,7,0,1,0,0],
    [9,8,0,0,0,1,3,7,0],
    [0,1,6,0,0,9,0,0,0],
    [0,0,9,2,0,6,7,0,0],
    [0,0,0,4,0,0,9,6,0],
    [0,2,3,6,0,0,0,1,7],
    [0,0,7,0,2,0,0,0,0],
    [1,9,0,0,0,0,0,0,2]]
findCell(s2,0,0)
for row in s2:
    for i in row:
        print(i," ", end="")
    print()
