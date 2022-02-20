# Minimum path by Dijkstra's algorithm
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

V=9
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
visited=[-1]*V
distance=[1000]*V
u=0
distance[u]=0
visited[u]=0
q=[i for i in range(0,9)]
while len(q)>0:
        u=q.pop(0)
        print(q,visited,distance)
        for v in q:
                a=distance[u]+graph[u][v]
                if graph[u][v]>0 and a<distance[v]:
                        distance[v]=a
                        visited[v]=0

print(q,visited,distance)
