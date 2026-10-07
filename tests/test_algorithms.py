from models.models import Delivery
from algorithms.graph import dijkstra
from algorithms.greedy import greedy_rank
from algorithms.knapsack import knapsack
from algorithms.scheduler import schedule_by_deadline


# ---------------------------------------------------------
# TEST 1: DIJKSTRA
# ---------------------------------------------------------

def test_dijkstra():

    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "D": 3},
        "C": {"A": 2, "D": 2},
        "D": {"B": 3, "C": 2, "E": 3},
        "E": {"D": 3}
    }

    result = dijkstra(graph, "A")

    assert result["A"] == 0
    assert result["B"] == 4
    assert result["C"] == 2
    assert result["D"] == 4
    assert result["E"] == 7


# ---------------------------------------------------------
# TEST 2: GREEDY RANKING
# ---------------------------------------------------------

def test_greedy_ranking():

    deliveries = [
        Delivery("D1", "A", "C", 4, 15, 500),
        Delivery("D2", "A", "D", 6, 12, 700),
        Delivery("D3", "B", "E", 3, 20, 400),
        Delivery("D4", "C", "E", 5, 18, 600)
    ]

    result = greedy_rank(deliveries)

    assert result[0].id == "D3"
    assert result[1].id == "D1"
    assert result[2].id == "D4"
    assert result[3].id == "D2"


# ---------------------------------------------------------
# TEST 3: 0/1 KNAPSACK
# ---------------------------------------------------------

def test_knapsack():

    deliveries = [
        Delivery("D1", "A", "C", 4, 15, 500),
        Delivery("D2", "A", "D", 6, 12, 700),
        Delivery("D3", "B", "E", 3, 20, 400),
        Delivery("D4", "C", "E", 5, 18, 600)
    ]

    selected, profit = knapsack(deliveries, 10)

    selected_ids = [delivery.id for delivery in selected]

    assert set(selected_ids) == {"D1", "D2"}
    assert profit == 1200


# ---------------------------------------------------------
# TEST 4: DEADLINE SCHEDULING
# ---------------------------------------------------------

def test_deadline_scheduling():

    deliveries = [
        Delivery("D1", "A", "C", 4, 15, 500),
        Delivery("D2", "A", "D", 6, 12, 700),
        Delivery("D3", "B", "E", 3, 20, 400),
        Delivery("D4", "C", "E", 5, 18, 600)
    ]

    result = schedule_by_deadline(deliveries)

    deadlines = [delivery.deadline for delivery in result]

    assert deadlines == [12, 15, 18, 20]


# ---------------------------------------------------------
# TEST 5: KNAPSACK CAPACITY
# ---------------------------------------------------------

def test_knapsack_capacity():

    deliveries = [
        Delivery("D1", "A", "C", 4, 15, 500),
        Delivery("D2", "A", "D", 6, 12, 700),
        Delivery("D3", "B", "E", 3, 20, 400),
        Delivery("D4", "C", "E", 5, 18, 600)
    ]

    selected, profit = knapsack(deliveries, 4)

    assert len(selected) == 1
    assert selected[0].id == "D1"
    assert profit == 500