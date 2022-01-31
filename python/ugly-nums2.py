# Find the first 'n' ugly numbers - take two

def find_ugly_nums(n):
    l=[]
    i2=0
    i3=0
    i5=0
    l.append(1)
    while len(l)<n:
        next=min(l[i2]*2, l[i3]*3, l[i5]*5)
        l.append(next)

        if next==l[i2]*2:
            i2+=1
        if next==l[i3]*3:
            i3+=1
        if next==l[i5]*5:
            i5+=1
    return l

result=find_ugly_nums(150)
print("\n",result)

        

