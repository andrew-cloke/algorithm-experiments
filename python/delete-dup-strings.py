# Delete duplicate strings in a list.

def removeDupStrings(s):
    words=[]
    word=""
    s+=" "
    for c in s:
        if c==" ":
            if len(words)>0 and words[-1]==word:
                words.pop()
            else:
                words.append(word)
            word=""
        else:
            word=word+c
    return len(words),words

print(removeDupStrings("one two two three"))
print(removeDupStrings("tom jerry jerry tom"))
print(removeDupStrings("ab aa aa bcd ab"))
