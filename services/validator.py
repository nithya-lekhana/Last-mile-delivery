def validate_plan(result, capacity):

    errors = []

    # Check capacity
    total_weight = sum(
        delivery.weight
        for delivery in result["selected"]
    )

    if total_weight > capacity:
        errors.append(
            f"Capacity exceeded: {total_weight}/{capacity}"
        )

    # Check deadlines
    for item in result["results"]:

        if item["completion_time"] > item["deadline"]:
            errors.append(
                f"{item['id']} missed deadline"
            )

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "total_weight": total_weight
    }