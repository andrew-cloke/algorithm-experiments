# Count possible decodings of a given Digit string

# A Binary Tree Node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def toChar(s):
    return chr(int(s)+64)

def decodeNextDigits(s,tree):
    if len(s)==0:
        return

    if len(s)==1 or s[1]!='0':   # If last char or not a following zero
        tree.left=Node(toChar(s[0]))
        decodeNextDigits(s[1:],tree.left)  # Recursively parse the string

    if len(s)>1 and int(s[0:2])<27:
        if len(s)>2 and s[2]=='0':
            return # No decode

        tree.right=Node(toChar(s[0:2]))
        decodeNextDigits(s[2:],tree.right)

def decodeDigitString(s):
    root=Node("")
    decodeNextDigits(s,root)
    return root

def printTreeRecursive(s,tree):
    s+=tree.data
    if tree.left==None and tree.right==None:  # Only print leaf nodes
        print(s)
    else:
        if tree.left!=None:
            printTreeRecursive(s,tree.left)
        if tree.right!=None:
            printTreeRecursive(s,tree.right)

def printTree(tree):
    s=""
    printTreeRecursive(s,tree)

print("121:")
root=decodeDigitString("121")
printTree(root)
print("1234:")
root=decodeDigitString("1234")
printTree(root)
print("1204:")
root=decodeDigitString("1204")
printTree(root)


        

