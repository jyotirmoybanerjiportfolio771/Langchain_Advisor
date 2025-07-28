from typing import TypedDict, List, Dict

class State(TypedDict):
    user_name: str
    goal: str
    portfolio: List[Dict]
    analysis: Dict
    recommendation: str
    preferred_channels: List[str]
