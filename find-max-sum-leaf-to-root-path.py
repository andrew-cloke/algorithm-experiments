# Python program to find maximum path sum in Binary Tree
 
# A Binary Tree Node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# This function returns overall maximum path sum in 'res'
# And returns max leaf to root sum
# It starts to calculate the sum from the leaf first,
# accumulating as the recursion unwinds and moves to the root
# This is fine for giving the sum, but not good for showing the path
# As you don't know the path to the root until the final recursion has unwound - at the root
def findLeafToRootMaxSum(root):
     
    # Base Case
    if root is None:
        return 0
    
    l=findLeafToRootMaxSum(root.left)
    r=findLeafToRootMaxSum(root.right)
    maxSumSoFar=max(l+root.data,r+root.data)
    print("Left",l,"Right",r,"Max so far",maxSumSoFar)
    return maxSumSoFar

def findLeafToRootMaxSumTopDown(node,sumSoFar):
    global maxSoFar
    global targetLeafNode

    if node == None:
        return

    sumSoFar+=node.data
    if sumSoFar > maxSoFar:
        maxSoFar=sumSoFar
        targetLeafNode=node

    print("Sum so far",sumSoFar,"Max so far",maxSoFar,"Node",node.data)
    maxSoFar=max(maxSoFar,sumSoFar)
    findLeafToRootMaxSumTopDown(node.left,sumSoFar)
    findLeafToRootMaxSumTopDown(node.right,sumSoFar)

def printPathToTarget(node):
    global targetLeafNode

    if node==None:
        return False

    if (printPathToTarget(node.left) or printPathToTarget(node.right) or node==targetLeafNode):
        print(node.data,end=" ")
        return True
    return False


# Driver program
root = Node(10)
root.left = Node(2)
root.right   = Node(10);
root.left.left  = Node(20);
root.left.right = Node(1);
root.right.right = Node(-25);
root.right.right.left   = Node(3);
root.right.right.right  = Node(4);
maxSoFar=-99999
findLeafToRootMaxSumTopDown(root,0)
print("Max sum from leaf to root is " ,maxSoFar)
print("Root from leaf to root is ", end="")
printPathToTarget(root)
print("")

# print("Max sum from leaf to root is " ,findLeafToRootMaxSum(root))
