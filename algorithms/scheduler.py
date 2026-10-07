def schedule_by_deadline(deliveries):
    return sorted(
        deliveries,
        key=lambda d: d.deadline
    )