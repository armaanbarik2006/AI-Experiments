import heapq
def a_star(graph,heuristic,start,goal):
    open_list =[(heuristic[start],start)]

    g_score = {node:float('inf')for node in graph}
    g_score[start]=0

    parent = {start:None}

    while open_list :
        _, current= heapq.heappop(open_list)

        if current== goal:
            path=[]
            while current is not None:
                path.append(current)
                current=parent[current]
            return path[::-1],g_score[goal]
        for neighbour,cost in graph[current]:
            tentative_g =g_score[current]+cost

            if tentative_g < g_score[neighbour]:
                g_score[neighbour] = tentative_g
                parent[neighbour]= current

                f_score= tentative_g + heuristic[neighbour]
                heapq.heappush(open_list,(f_score,neighbour))

    return None, float('inf')

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# Heuristic values: estimated distance to goal D
heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

start = 'A'
goal = 'D'

path, cost = a_star(graph, heuristic, start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found")
