# Decode string with nested repeats - 1 stack approach
# E.g. "1[b]" -> "b"; "2[a3[b]]" -> "abbbabbb"

def decode(s):
    charStack=[]
    for c in s:
        if c == ']':
            # Build repeat string
            repeatStr=""
            c=charStack.pop()
            while c != '[':
                repeatStr=c+repeatStr
                c=charStack.pop()
            # Build repeat count
            count=0
            count_pos=1
            while True:
                if len(charStack)>0:
                    c=charStack.pop()
                    if c.isdigit():
                        count+=int(c)*count_pos
                        count_pos*=10
                    else:
                        charStack.append(c)
                        break
                else:
                    break
            charStack.append(repeatStr*count)
        else:
            charStack.append(c)
    return str.join('',charStack)

print(decode("2[a3[bc]]21[d]"))
        
