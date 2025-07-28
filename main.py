from .graph import graph

input_state = {
    "user_name": "Ravi",
    "goal": "Retirement in 15 years",
    "portfolio": [
        {"type": "Equity", "name": "AXISBANK.BO", "amount": 400000},
        {"type": "Debt", "name": "ICICIBANK.BO", "amount": 150000},
        {"type": "Gold", "name": "GOLDBEES.BO", "amount": 50000}
    ],
    "preferred_channels": ["print"]
}

graph.invoke(input_state)
