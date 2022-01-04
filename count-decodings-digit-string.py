# Count possible decodings of a given Digit string

# 1,1,1,1,
# 2,2,2,2

def decodeDigitString(s):
    j=1
    while True:
        i=0
        word=""
        for c in s:
            word+=c
            i+=1
            if i==j:
                num=int(word)
                if num<27:
                    print(chr(num+64),end="")
                i=0


        

