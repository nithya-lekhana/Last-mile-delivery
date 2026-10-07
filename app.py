import json
import streamlit as st
import streamlit.components.v1 as components

from data.io import load_json
from models.models import Delivery
from services.optimizer import optimize_deliveries
from services.validator import validate_plan
from algorithms.greedy import greedy_rank


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Last-Mile Delivery Optimizer",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    color: #1e293b;
    margin-top: 25px;
    margin-bottom: 12px;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    text-align: center;
}

.metric-label {
    font-size: 14px;
    color: #64748b;
    margin-bottom: 8px;
}

.metric-value {
    font-size: 28px;
    font-weight: 700;
    color: #1e3a8a;
}

.valid-value {
    color: #15803d;
}

.invalid-value {
    color: #dc2626;
}

.route-box {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    padding: 18px;
    border-radius: 12px;
    font-size: 20px;
    font-weight: 600;
    color: #1e40af;
    text-align: center;
    margin-top: 10px;
}

.info-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px;
    height: 100%;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.info-card h4 {
    color: #1e3a8a;
    margin-bottom: 8px;
}

.info-card p {
    color: #475569;
    font-size: 14px;
    line-height: 1.6;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    padding: 30px 0 10px 0;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("Last-Mile Delivery Optimization")

st.write(
    "Intelligent route planning and delivery scheduling "
    "using classical Design and Analysis of Algorithms."
)

st.markdown(
    """
    **Dijkstra** &nbsp; | &nbsp;
    **Greedy** &nbsp; | &nbsp;
    **Dynamic Programming** &nbsp; | &nbsp;
    **Deadline Scheduling**
    """
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("Vehicle Settings")

    capacity = st.number_input(
        "Vehicle Capacity",
        min_value=1,
        value=10,
        step=1
    )

    st.divider()

    st.subheader("Algorithm Pipeline")

    st.write("1. Greedy Ranking")
    st.write("2. 0/1 Knapsack DP")
    st.write("3. Deadline Scheduling")
    st.write("4. Dijkstra Routing")
    st.write("5. Plan Validation")

    st.divider()

    st.caption(
        "Project: Last-Mile Delivery with Deadlines"
    )


# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

with open("data/graph.json", "r") as file:
    graph = json.load(file)

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


# ---------------------------------------------------------
# AVAILABLE DELIVERIES
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">Available Deliveries</div>',
    unsafe_allow_html=True
)

st.dataframe(
    orders,
    use_container_width=True,
    hide_index=True
)


# ---------------------------------------------------------
# DELIVERY NETWORK
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">Delivery Network</div>',
    unsafe_allow_html=True
)

network_html = """
<div style="
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 15px;
">

<svg width="100%" height="300" viewBox="0 0 800 300">

    <!-- Edges -->

    <line x1="150" y1="150"
          x2="350" y2="70"
          stroke="#64748b"
          stroke-width="4"/>

    <line x1="150" y1="150"
          x2="350" y2="230"
          stroke="#64748b"
          stroke-width="4"/>

    <line x1="350" y1="70"
          x2="550" y2="150"
          stroke="#64748b"
          stroke-width="4"/>

    <line x1="350" y1="230"
          x2="550" y2="150"
          stroke="#64748b"
          stroke-width="4"/>

    <line x1="550" y1="150"
          x2="700" y2="150"
          stroke="#64748b"
          stroke-width="4"/>


    <!-- Edge weights -->

    <text x="245" y="100"
          font-size="18"
          fill="#334155"
          text-anchor="middle">4</text>

    <text x="245" y="215"
          font-size="18"
          fill="#334155"
          text-anchor="middle">2</text>

    <text x="450" y="100"
          font-size="18"
          fill="#334155"
          text-anchor="middle">3</text>

    <text x="450" y="215"
          font-size="18"
          fill="#334155"
          text-anchor="middle">2</text>

    <text x="625" y="140"
          font-size="18"
          fill="#334155"
          text-anchor="middle">3</text>


    <!-- Nodes -->

    <circle cx="150" cy="150"
            r="32"
            fill="#2563eb"/>

    <circle cx="350" cy="70"
            r="32"
            fill="#2563eb"/>

    <circle cx="350" cy="230"
            r="32"
            fill="#2563eb"/>

    <circle cx="550" cy="150"
            r="32"
            fill="#2563eb"/>

    <circle cx="700" cy="150"
            r="32"
            fill="#2563eb"/>


    <!-- Node labels -->

    <text x="150" y="157"
          text-anchor="middle"
          font-size="20"
          font-weight="bold"
          fill="white">A</text>

    <text x="350" y="77"
          text-anchor="middle"
          font-size="20"
          font-weight="bold"
          fill="white">B</text>

    <text x="350" y="237"
          text-anchor="middle"
          font-size="20"
          font-weight="bold"
          fill="white">C</text>

    <text x="550" y="157"
          text-anchor="middle"
          font-size="20"
          font-weight="bold"
          fill="white">D</text>

    <text x="700" y="157"
          text-anchor="middle"
          font-size="20"
          font-weight="bold"
          fill="white">E</text>

</svg>

</div>
"""

components.html(
    network_html,
    height=330
)

st.caption(
    "Weighted delivery network used by Dijkstra's shortest-path algorithm."
)


# ---------------------------------------------------------
# GREEDY RANKING
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">Greedy Profit-to-Weight Ranking</div>',
    unsafe_allow_html=True
)

greedy_result = greedy_rank(deliveries)

greedy_data = []

for delivery in greedy_result:

    ratio = delivery.profit / delivery.weight

    greedy_data.append({
        "Delivery": delivery.id,
        "Profit": delivery.profit,
        "Weight": delivery.weight,
        "Profit / Weight": round(ratio, 2)
    })

st.dataframe(
    greedy_data,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Deliveries are ranked by profit-to-weight ratio. "
    "The final capacity-constrained selection is determined "
    "using 0/1 Knapsack Dynamic Programming."
)


# ---------------------------------------------------------
# OPTIMIZATION BUTTON
# ---------------------------------------------------------

st.markdown("")


# Initialize session state

if "result" not in st.session_state:
    st.session_state.result = None

if "validation" not in st.session_state:
    st.session_state.validation = None


# Optimization button

if st.button(
    "Run Delivery Optimization",
    type="primary",
    use_container_width=True
):

    st.session_state.result = optimize_deliveries(
        deliveries,
        graph,
        capacity
    )

    st.session_state.validation = validate_plan(
        st.session_state.result,
        capacity
    )


# Get stored results

result = st.session_state.result
validation = st.session_state.validation


# ---------------------------------------------------------
# DISPLAY RESULTS
# ---------------------------------------------------------

if result is not None and validation is not None:

    # -----------------------------------------------------
    # METRICS
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Optimization Result</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)


    # Maximum Profit

    with col1:

        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">Maximum Profit</div>
                <div class="metric-value">₹{}</div>
            </div>
            """.format(result["total_profit"]),
            unsafe_allow_html=True
        )


    # Vehicle Load

    with col2:

        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">Vehicle Load</div>
                <div class="metric-value">{}/{}</div>
            </div>
            """.format(
                validation["total_weight"],
                capacity
            ),
            unsafe_allow_html=True
        )


    # Travel Time

    with col3:

        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">Travel Time</div>
                <div class="metric-value">{}</div>
            </div>
            """.format(result["total_time"]),
            unsafe_allow_html=True
        )


    # Plan Status

    with col4:

        status_class = (
            "valid-value"
            if validation["valid"]
            else "invalid-value"
        )

        status_text = (
            "VALID"
            if validation["valid"]
            else "INVALID"
        )

        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-label">Plan Status</div>
                <div class="metric-value {}">{}</div>
            </div>
            """.format(
                status_class,
                status_text
            ),
            unsafe_allow_html=True
        )


    # -----------------------------------------------------
    # DYNAMIC PROGRAMMING SELECTION
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">0/1 Knapsack Selection</div>',
        unsafe_allow_html=True
    )

    st.info(
        f"Dynamic Programming selected "
        f"{len(result['selected'])} deliveries with a total "
        f"profit of ₹{result['total_profit']} within the "
        f"vehicle capacity of {capacity}."
    )


    # -----------------------------------------------------
    # SELECTED DELIVERIES
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Selected Deliveries</div>',
        unsafe_allow_html=True
    )

    selected_data = []

    for delivery in result["selected"]:

        selected_data.append({
            "Delivery": delivery.id,
            "Pickup": delivery.pickup,
            "Drop": delivery.drop,
            "Weight": delivery.weight,
            "Profit": delivery.profit,
            "Deadline": delivery.deadline
        })

    st.dataframe(
        selected_data,
        use_container_width=True,
        hide_index=True
    )


    # -----------------------------------------------------
    # OPTIMIZED ROUTE
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Optimized Route</div>',
        unsafe_allow_html=True
    )

    route_text = " → ".join(result["route"])

    st.markdown(
        f"""
        <div class="route-box">
            {route_text}
        </div>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # DELIVERY SCHEDULE
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Delivery Schedule</div>',
        unsafe_allow_html=True
    )

    schedule_data = []

    for item in result["results"]:

        status = (
            "On Time"
            if item["completion_time"] <= item["deadline"]
            else "Late"
        )

        schedule_data.append({
            "Delivery": item["id"],
            "Deadline": item["deadline"],
            "Completion Time": item["completion_time"],
            "Status": status
        })

    st.dataframe(
        schedule_data,
        use_container_width=True,
        hide_index=True
    )


    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if validation["valid"]:

        st.success(
            "The optimized delivery plan is valid. "
            "All selected deliveries satisfy the capacity "
            "and deadline constraints."
        )

    else:

        st.error(
            "The optimized delivery plan is invalid."
        )

        for error in validation["errors"]:

            st.error(error)


    # -----------------------------------------------------
    # ALGORITHM EXPLANATION
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">Algorithms Used</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)


    # Greedy

    with c1:

        st.markdown(
            """
            <div class="info-card">
                <h4>Greedy Algorithm</h4>
                <p>
                    Ranks deliveries using the profit-to-weight
                    ratio to identify attractive delivery options.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


    # Knapsack

    with c2:

        st.markdown(
            """
            <div class="info-card">
                <h4>0/1 Knapsack</h4>
                <p>
                    Uses dynamic programming to select the
                    combination of deliveries that maximizes
                    profit within vehicle capacity.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


    # Dijkstra

    with c3:

        st.markdown(
            """
            <div class="info-card">
                <h4>Dijkstra</h4>
                <p>
                    Computes shortest travel paths between
                    pickup and drop locations using the
                    weighted delivery graph.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


    # Deadline Scheduling

    with c4:

        st.markdown(
            """
            <div class="info-card">
                <h4>Deadline Scheduling</h4>
                <p>
                    Arranges selected deliveries according to
                    their earliest deadlines to prioritize
                    time-sensitive deliveries.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Last-Mile Delivery Optimization |
        Design and Analysis of Algorithms Project
    </div>
    """,
    unsafe_allow_html=True
)