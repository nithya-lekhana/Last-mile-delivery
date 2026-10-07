import json

from data.io import load_json
from models.models import Delivery
from services.optimizer import optimize_deliveries
from services.validator import validate_plan
from services.report import print_report


def main():

    # Load graph
    with open("data/graph.json", "r") as file:
        graph = json.load(file)

    # Load delivery orders
    orders = load_json("data/orders.json")

    # Convert JSON data into Delivery objects
    deliveries = [
        Delivery(
            order["id"],
            order["pickup"],
            order["drop"],
            order["weight"],
            order["deadline"],
            order["profit"]
        )
        for order in orders
    ]

    # Vehicle capacity
    capacity = 10

    # Optimize deliveries
    result = optimize_deliveries(
        deliveries,
        graph,
        capacity
    )

    # Validate final plan
    validation = validate_plan(
        result,
        capacity
    )

    # Display final report
    print_report(
        result,
        validation
    )


if __name__ == "__main__":
    main()