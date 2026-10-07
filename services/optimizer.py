from algorithms.knapsack import knapsack
from algorithms.scheduler import schedule_by_deadline
from algorithms.graph import dijkstra


def optimize_deliveries(deliveries, graph, capacity):

    # Step 1: Select deliveries using DP
    selected, total_profit = knapsack(
        deliveries,
        capacity
    )

    # Step 2: Arrange selected deliveries by deadline
    scheduled = schedule_by_deadline(selected)

    current_node = "A"
    total_time = 0
    route = [current_node]

    results = []

    # Step 3: Calculate travel time using Dijkstra
    for delivery in scheduled:

        # Travel from current location to pickup
        distances = dijkstra(graph, current_node)
        pickup_time = distances[delivery.pickup]

        total_time += pickup_time
        current_node = delivery.pickup

        # Travel from pickup to drop
        distances = dijkstra(graph, current_node)
        delivery_time = distances[delivery.drop]

        total_time += delivery_time
        current_node = delivery.drop

        route.append(current_node)

        results.append({
            "id": delivery.id,
            "pickup": delivery.pickup,
            "drop": delivery.drop,
            "deadline": delivery.deadline,
            "completion_time": total_time,
            "profit": delivery.profit
        })

    return {
        "selected": selected,
        "total_profit": total_profit,
        "route": route,
        "total_time": total_time,
        "results": results
    }