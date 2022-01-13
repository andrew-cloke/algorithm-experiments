# Travelling Saleman Problem with a Recursive solution

def allVisited(a):
    for i in a:
        if not i:
            return False
    return True

def tsp(graph,curr_pos,visited,cost):
    global nodes
    global ans

    if allVisited(visited):
        cost+=graph[curr_pos][0]
        ans.append(cost)
        return
    
    for i in range(nodes):
        if not visited[i]:
            cost+=graph[curr_pos][i]
            visited[i]=True
            tsp(graph,i,visited,cost)
            visited[i]=False


# Driver Code
if __name__ == "__main__":
    nodes=4
    ans=[]
    # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
    visited=[ False,False,False,False ]
    tsp(graph, 0, visited,0)
    print(ans)
