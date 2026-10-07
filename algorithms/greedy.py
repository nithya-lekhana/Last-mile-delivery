def greedy_rank(deliveries):
    return sorted(
        deliveries,
        key=lambda d: d.profit / d.weight,
        reverse=True
    )