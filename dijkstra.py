# dijkstra.py - Shortest Path using Dijkstra's Algorithm
import heapq

def dijkstra(graph, start, target):
    pq = []  # Priority queue
    heapq.heappush(pq, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parents = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node == target:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parents[current_node]
            return distances[target], path[::-1]
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    return float('inf'), []

graph = {
    "A": [("F", 14), ("C", 9), ("B", 7)],
    "B": [("A", 7), ("C", 10), ("D", 15)],
    "C": [("A", 9), ("F", 2), ("B", 10), ("D", 11)],
    "D": [("B", 15), ("C", 11), ("E", 6)],
    "E": [("F", 9), ("D", 6)],
    "F": [("A", 14), ("C", 2), ("E", 9)]
}

print(dijkstra(graph, "A", "F"))
