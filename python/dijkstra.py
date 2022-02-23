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
distance=[1000]*V
q=[i for i in range(0,9)]
u=0
distance[u]=0
while len(q)>0:
        print(u,q,distance)
# Find the distance from u to each connected node and update if minimum
        for v in q:
                a=distance[u]+graph[u][v]
                if graph[u][v]>0 and a<distance[v]:
                        distance[v]=a
# Remove the visited node from the list
        q.remove(u)
# Process the unvisited node with the minimum distance next 
        min=1000
        for v in q:
                if distance[v]<min:
                        min=distance[v]
                        u=v

print(distance)
