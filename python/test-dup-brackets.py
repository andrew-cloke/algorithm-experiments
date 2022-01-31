# Test to see if an expression has duplicate paranthesis

def testDupBrackets(s):
    exprStack=[]
    for c in s:
        if c==')':
            count=0
            while True:
                if len(exprStack)==0:
                    break
                count+=1
                c=exprStack.pop()
                if c=='(':
                    break
            if count==1:
                return True
        else:
            exprStack.append(c)
    return False

print(testDupBrackets("(((a+(b)))+(c+d))"))
print(testDupBrackets("((a+b)+(c+d))"))
print(testDupBrackets("((a+(b))+(c+d))"))
        