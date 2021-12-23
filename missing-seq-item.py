#!/usr/bin/env python
import random
import math

def CreateTestSeq(listSize):
    testSeq=[i for i in range(listSize)]
    del testSeq[random.randint(0,listSize-1)]
    return testSeq

seqLength=100
a=CreateTestSeq(seqLength)
print(a)

found=False
i=seqLength-1
offset=0
iteration=0
while not found:
    iteration+=1
    if a[offset]==offset and a[offset+1]!=offset+1:
        found=True
    i=math.ceil(i/2)
    if a[offset+i]>offset+i:  # if True, gap must be in first half
        print("Iteration #",iteration," Missing number in first half ",i,offset)
    else:
        offset+=i
        print("Iteration #", iteration," Missing number in second half ",i,offset)

print("Missing number is ",offset+1)

