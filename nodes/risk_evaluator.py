def risk_evaluator(state):
    breakdown = state["analysis"]["breakdown"]
    risk_flags = []

    if breakdown.get("Equity", 0) > 70:
        risk_flags.append("High equity exposure.")
    if "Gold" in breakdown and breakdown["Gold"] < 5:
        risk_flags.append("Gold hedge is too low.")

    state["analysis"]["risks"] = risk_flags
    return state
