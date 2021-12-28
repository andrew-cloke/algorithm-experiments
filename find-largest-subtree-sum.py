# Python program to find maximum path sum in Binary Tree
 
# A Binary Tree Node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# This function returns overall maximum path sum in 'res'
# And returns max path sum going through root
def findSubTreeSum(root):
     
    # Base Case
    if root is None:
        return 0

    # Iterate through each subtree left and right
    l = findSubTreeSum(root.left)
    r = findSubTreeSum(root.right)

    subTreeSum=l+r+root.data
    findSubTreeSum.result=max(findSubTreeSum.result,subTreeSum)
    print("This subtree",subTreeSum,"Left", l, "Right",r,"Overall max",findSubTreeSum.result)
    return subTreeSum

def findMaxSubTreeSum(root):
    findSubTreeSum.result=float("-inf")
    findSubTreeSum(root)
    return findSubTreeSum.result

# Driver program
root = Node(1)
root.left = Node(-2)
root.right   = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)
root.right.left  = Node(-6)
root.right.right = Node(2)
print("Max path sum is " ,findMaxSubTreeSum(root))
