# Python program to find all Binary Tree paths that sum to a value 'k'

def populateTestTree1():
    root = Node(10)
    root.left = Node(2)
    root.right   = Node(10)
    root.left.left  = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left   = Node(3)
    root.right.right.right  = Node(4)
    return root

def populateTestTree2():
    root = Node(1)
    root.left = Node(-2)
    root.right   = Node(3)
    root.left.left  = Node(4)
    root.left.right = Node(5)
    root.right.left  = Node(-6)
    root.right.right = Node(2)
    return root

def populateTestTree3():
    root = Node(1)
    root.left = Node(3)
    root.right   = Node(-1)
    root.left.left  = Node(2)
    root.left.right = Node(1)
    root.left.right.left = Node(1)
    root.right.left  = Node(4)
    root.right.left.left  = Node(1)
    root.right.left.right  = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(6)
    return root

# A Binary Tree Node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sumList(list):
    total=0
    for i in list:
        total+=i
    return total

def testQueue(queue):
    global k

    subQueue=queue.copy()
    total=0
    while len(subQueue)>0:
        if sumList(subQueue)==k:
            print("Found",subQueue)
        subQueue.pop(0)

    return

def walkTreeTopDown(node,queue):
    if node == None:
        return
    
    queue.append(node.data)
    testQueue(queue)
    
    walkTreeTopDown(node.left,queue)
    walkTreeTopDown(node.right,queue)
    queue.pop()

# Driver program
root=populateTestTree3()
k=5
sumQueue=[]
walkTreeTopDown(root,sumQueue)
