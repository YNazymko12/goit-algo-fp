import heapq

def dijkstra(graph, start):
    # Ініціалізація
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Ініціалізація пріоритетної черги
    priority_queue = [(0, start)]

    while priority_queue:
        # Витягуємо вершину з найменшою відстанню
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо знайдена відстань більша за збережену, продовжуємо
        if current_distance > distances[current_node]:
            continue

        # Перебираємо сусідів
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Якщо знайдена менша відстань, оновлюємо її
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

def create_graph():
    # Створення графа у вигляді списку суміжностей
    graph = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2, "D": 5},
        "C": {"A": 4, "B": 2, "D": 1},
        "D": {"B": 5, "C": 1},
    }
    return graph

def main():
    graph = create_graph()
    start = "A"
    distances = dijkstra(graph, start)
    
    for node, distance in distances.items():
        print(f"Відстань від {start} до {node}: {distance}")

if __name__ == "__main__":
    main()