# Hamiltonian Cycle attempt #2

def allVisited(v):
    for i in v:
        if not i:
            return False
    return True

def tryNextPath(graph,curr_pos,v,p):
    if allVisited(v) and graph[curr_pos][0]==1:
        p.append(0)
        print(p)
        p.pop()
        return

    for i in range(0,5):
        if not v[i] and graph[curr_pos][i]==1:
            p.append(i)
            v[i]=True
            tryNextPath(graph,i,v,p)
            p.pop()
            v[i]=False

if __name__=="__main__":
    graph=[ [0,1,0,1,0],
            [1,0,1,1,1],
            [0,1,0,0,1],
            [1,1,0,0,1],
            [0,0,1,1,0]]
    visited=[True, False, False, False, False]
    path=[0]
    tryNextPath(graph,0,visited,path)