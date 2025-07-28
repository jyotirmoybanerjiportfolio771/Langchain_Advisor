from langgraph.graph import StateGraph, END
from .state import State
from .nodes.portfolio_parser import portfolio_parser
from .nodes.market_analyzer import market_analyzer
from .nodes.risk_evaluator import risk_evaluator
from .nodes.recommendation_ai import recommendation_ai
from .nodes.notifier import notifier

builder = StateGraph(State)

builder.add_node("start", portfolio_parser)
builder.add_node("portfolio_parser", portfolio_parser)
builder.add_node("market_analyzer", market_analyzer)
builder.add_node("risk_evaluator", risk_evaluator)
builder.add_node("recommendation_ai", recommendation_ai)
builder.add_node("notifier", notifier)

builder.set_entry_point("start")
builder.add_edge("start", "portfolio_parser")
builder.add_edge("portfolio_parser", "market_analyzer")
builder.add_edge("market_analyzer", "risk_evaluator")
builder.add_edge("risk_evaluator", "recommendation_ai")
builder.add_edge("recommendation_ai", "notifier")
builder.add_edge("notifier", END)

graph = builder.compile()
