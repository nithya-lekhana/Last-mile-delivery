import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances