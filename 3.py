import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 7, 'C': 9,},
    'B': {'A': 7, 'C': 10, 'D': 15},
    'C': {'A': 9, 'B': 10, 'D': 11,},
    'D': {'B': 15, 'C': 11, 'E': 6},
    'E': {'D': 6, 'A': 9}
}

shortest_paths = dijkstra(graph, 'A')

for vertex, distance in shortest_paths.items():
    print(f"Відстань від {'A'} до {vertex} дорівнює {distance}")
