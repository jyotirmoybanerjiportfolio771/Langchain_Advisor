from ..llm_utils import call_mistral

def recommendation_ai(state):
    prompt = f"""
User Goal: {state['goal']}
Portfolio Breakdown: {state['analysis']['breakdown']}
Risks: {state['analysis']['risks']}
Give a concise portfolio recommendation.
"""
    state["recommendation"] = call_mistral(prompt)
    return state
