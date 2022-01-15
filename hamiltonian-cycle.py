# Check a given graph for a Hamiltonian cycle
# https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/?ref=lbp

def allVisited(a):
    for i in a:
        if not i:
            return False
    return True

def hamlton_check(graph,curr_pos,visited):
    global nodes
    global path
    global found

    if allVisited(visited):
        print("Path",path)
        if graph[curr_pos][0]==1:
            found=True
    
    for i in range(nodes):
        if not visited[i] and graph[curr_pos][i]==1:
            path.append((curr_pos,i))
            visited[i]=True
            hamlton_check(graph,i,visited)
            path.pop()
            visited[i]=False

# Driver Code
if __name__ == "__main__":
    found=False
    nodes=5
    path=[]
    # matrix representation of graph
    graph1 = [[0, 1, 0, 1, 0],
            [ 1, 0, 1, 1, 1],
            [ 0, 1, 0, 0, 1],
            [ 1, 1, 0, 0, 1],
            [ 0, 1, 1, 1, 0]]
    visited=[ False] * nodes
    visited[0]=True
    hamlton_check(graph1, 0, visited)
    print("Graph1",found)

    found=False
    graph2 = [[0, 1, 0, 1, 0],
            [ 1, 0, 1, 1, 1],
            [ 0, 1, 0, 0, 1],
            [ 1, 1, 0, 0, 0],
            [ 0, 1, 1, 0, 0]]
    visited=[ False] * nodes
    visited[0]=True
    hamlton_check(graph2, 0, visited)
    print("Graph2",found)

