def print_report(result, validation):

    print("\n" + "=" * 50)
    print("       LAST-MILE DELIVERY OPTIMIZATION")
    print("=" * 50)

    print("\nSelected Deliveries:")

    for delivery in result["selected"]:
        print(
            f"{delivery.id} | "
            f"{delivery.pickup} -> {delivery.drop} | "
            f"Weight: {delivery.weight} | "
            f"Profit: {delivery.profit}"
        )

    print("\nTotal Profit:", result["total_profit"])

    print("\nRoute:")
    print(" -> ".join(result["route"]))

    print("\nDelivery Schedule:")

    for item in result["results"]:
        status = (
            "On Time"
            if item["completion_time"] <= item["deadline"]
            else "Late"
        )

        print(
            f"{item['id']} | "
            f"Deadline: {item['deadline']} | "
            f"Completion: {item['completion_time']} | "
            f"{status}"
        )

    print("\nTotal Weight:", validation["total_weight"])
    print("Total Travel Time:", result["total_time"])

    print("\nPlan Status:", "VALID" if validation["valid"] else "INVALID")

    if validation["errors"]:
        print("\nErrors:")

        for error in validation["errors"]:
            print("-", error)

    print("\n" + "=" * 50)