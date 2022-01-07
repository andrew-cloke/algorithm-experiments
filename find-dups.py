#!/usr/bin/env python

import random
import math

def CreateTestSeq(listSize,numDups):
    testSeq=[i for i in range(listSize)]
    for i in range(numDups):
        indexOrg=random.randint(0,listSize-1)
        indexDup=random.randint(0,listSize-1)
        testSeq[indexDup]=testSeq[indexOrg]
        print("Duplicating ",indexOrg,indexDup)
    return testSeq

seqLength=100
a=CreateTestSeq(seqLength,4)
print(a)

for i in range(seqLength):
    for j in range(i+1,seqLength):
        if a[i]==a[j]:
            print("Found dup ",a[i],"Indexes",i,j)