# Last-Mile Delivery Optimization

## Project Overview

Last-Mile Delivery Optimization is a Design and Analysis of Algorithms (DAA) project that plans delivery routes while considering vehicle capacity, delivery deadlines, travel time, and delivery profit.

The system combines multiple algorithms to select profitable deliveries, schedule them according to deadlines, calculate shortest travel paths, and validate the final delivery plan.

## Problem Statement

Given a set of pickup and delivery requests with different weights, deadlines, and profits, determine a feasible delivery plan for a vehicle with limited capacity while maximizing total profit and minimizing unnecessary travel.

## Objectives

- Select deliveries within vehicle capacity.
- Maximize total delivery profit.
- Prioritize deliveries using profit-to-weight ratio.
- Schedule selected deliveries according to deadlines.
- Find shortest travel paths between locations.
- Validate capacity and deadline constraints.
- Provide an interactive interface for the optimization process.

## Algorithms Used

### 1. Greedy Algorithm

Deliveries are ranked according to their profit-to-weight ratio:

`Profit / Weight`

This provides a heuristic priority for comparing delivery opportunities.

**Time Complexity:** O(n log n)

### 2. 0/1 Knapsack Dynamic Programming

The Knapsack algorithm selects the combination of deliveries that produces the maximum total profit without exceeding vehicle capacity.

**Time Complexity:** O(nC)

where:

- `n` = number of deliveries
- `C` = vehicle capacity

### 3. Earliest Deadline First Scheduling

Selected deliveries are ordered according to their deadlines so that deliveries with earlier deadlines are handled first.

**Time Complexity:** O(n log n)

### 4. Dijkstra's Algorithm

Dijkstra's algorithm calculates the shortest travel distance/time between locations in the delivery network.

**Time Complexity:** O((V + E) log V)

where:

- `V` = number of vertices
- `E` = number of edges

### 5. Plan Validation

The final plan is checked against vehicle capacity and delivery deadline constraints.

**Time Complexity:** O(n)

## System Workflow

```text
Delivery Input
      |
      v
Greedy Ranking
      |
      v
0/1 Knapsack DP
      |
      v
Selected Deliveries
      |
      v
Deadline Scheduling
      |
      v
Dijkstra Shortest Path
      |
      v
Plan Validation
      |
      v
Final Delivery Plan
```

## Project Structure

```text
Last-Mile-Delivery/
│
├── algorithms/
│   ├── graph.py
│   ├── greedy.py
│   ├── knapsack.py
│   └── scheduler.py
│
├── data/
│   ├── graph.json
│   ├── io.py
│   └── orders.json
│
├── models/
│   └── models.py
│
├── services/
│   ├── optimizer.py
│   ├── report.py
│   └── validator.py
│
├── tests/
│   └── test_algorithms.py
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

## Technologies Used

- Python
- Streamlit
- Dynamic Programming
- Greedy Algorithms
- Graph Algorithms
- Dijkstra's Algorithm
- Pytest
- JSON

## Running the Project Locally

### 1. Create and activate the virtual environment

```bash
python -m venv .venv
```

Windows:

```cmd
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the command-line version

```bash
python main.py
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

## Running Tests

Run:

```bash
python -m pytest -q
```

The project contains automated tests for:

- Dijkstra's algorithm
- Greedy ranking
- 0/1 Knapsack
- Deadline scheduling
- Capacity-based selection

## Sample Result

For the provided sample data and vehicle capacity of 10:

```text
Selected Deliveries:
D1 | A -> C | Weight: 4 | Profit: 500
D2 | A -> D | Weight: 6 | Profit: 700

Total Profit: 1200
Total Weight: 10
Total Travel Time: 10

Plan Status: VALID
```

## Deployment

The project includes a Streamlit interface and can be deployed using a Streamlit-compatible hosting platform.

The main application entry point is:

```text
app.py
```

Dependencies are specified in:

```text
requirements.txt
```

## Limitations

- The system models a single vehicle.
- Travel times are static.
- Live traffic conditions are not considered.
- GPS data is not used.
- The system does not claim global optimality for the complete routing and scheduling problem.
- The optimization model is designed as an academic DAA implementation.

## Future Scope

- Multiple vehicle optimization
- Real-time traffic integration
- GPS-based route tracking
- Time-window constraints
- Vehicle-specific capacities
- Multi-depot delivery optimization
- Advanced vehicle routing algorithms
- Real-time delivery status updates

## Testing

The project uses Pytest for automated algorithm testing.

Example:

```text
5 passed
```

## Academic Project

**Project:** Last-Mile Delivery Optimization  
**Domain:** Design and Analysis of Algorithms  
**Language:** Python  
**Interface:** Streamlit
`
