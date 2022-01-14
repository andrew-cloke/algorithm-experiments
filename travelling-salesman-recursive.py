# Travelling Saleman Problem with a Recursive solution

def allVisited(a):
    for i in a:
        if not i:
            return False
    return True

def tsp(graph,curr_pos,visited,cost):
    global nodes
    global ans
    global path

    if allVisited(visited):
        cost+=graph[curr_pos][0]
        ans.append(cost)
        print("Final cost",cost,"Path",path)
        return
    
    for i in range(nodes):
        if not visited[i]:
            path.append((curr_pos+1,i+1))
            visited[i]=True
            tsp(graph,i,visited,cost+graph[curr_pos][i])
            path.pop()
            visited[i]=False


# Driver Code
if __name__ == "__main__":
    nodes=4
    ans=[]
    path=[]
    # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
    visited=[ True,False,False,False ]
    tsp(graph, 0, visited,0)
    print(ans)
