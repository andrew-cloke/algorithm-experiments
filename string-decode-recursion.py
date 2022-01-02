# Decode string with nested repeats
# E.g. "1[b]" -> "b"; "2[a3[b]]" -> "abbbabbb"

import re

def decode(s):
    print("Decode",s)
    count=1
    if re.match('[a-z]+$',s):
        print("Simple case",s)
        return s

    countStr=re.search('[0-9]+',s).group()
    count=int(countStr)
    startStr=re.search('[0-9]+\[',s).end()
    startCount=re.search('[0-9]+\[',s).start()
    print("Start of repeat count",startCount)
    endStr=s.rfind(']')
    leadingStr=s[:startCount]
    trailingStr=s[endStr+1:]
    nextIterationStr=s[startStr:endStr]
    repeatedStr=decode(nextIterationStr)   # strip away the trailing ']'
    
    print("Repeat String",repeatedStr,count,"times with ",leadingStr,"leading string and ",trailingStr,"trailing string ",end='')
    s=leadingStr+repeatedStr*count+trailingStr
    print("giving",s)
    return s

print(decode("a2[b2[c]]d"))

