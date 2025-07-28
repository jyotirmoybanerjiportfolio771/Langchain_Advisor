import yfinance as yf

def market_analyzer(state):
    for p in state["portfolio"]:
        try:
            data = yf.Ticker(p["name"]).info
            p["performance"] = data.get("fiveYearAvgReturn", "N/A")
        except:
            p["performance"] = "Unknown"
    return state
