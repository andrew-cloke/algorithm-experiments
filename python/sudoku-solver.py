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

def createPossibilityMatrix(s):
    matrix=[]
    for i in range(0,9):
        a=[]
        for j in range(0,9):
            b=[]
            if s[i][j]==0:
                for k in range(1,10):
                    if not findNum(s,i,j,k):
                        b.append(k)
            a.append(b)
        matrix.append(a)
    return matrix

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
    global rollback
    (i,j)=findNextEmptyCell(s,i,j)
    if j==9:
        print(s)
        return True
    p=createPossibilityCell(s,i,j)
    if len(p)==0:
        return False
    print(i,j)
    for v in p:
        s[i][j]=v
        finish=findCell(s,i,j)
        if finish:
            return True
    s[i][j]=0

s=[[5,9,0,0,8,4,0,0,0],
   [0,4,0,0,0,0,0,6,9],
   [0,0,0,1,9,0,8,4,0],
   [0,0,0,2,3,6,4,5,8],
   [3,0,2,0,0,0,6,0,0],
   [0,0,0,0,0,0,3,0,0],
   [0,2,0,3,0,7,9,0,4],
   [0,3,0,0,1,0,0,0,0],
   [6,0,0,5,4,0,0,3,0]]
rollback=[]
findCell(s,0,0)