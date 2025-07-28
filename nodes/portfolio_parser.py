def portfolio_parser(state):
    total = sum(p['amount'] for p in state['portfolio'])
    breakdown = {p['type']: round(p['amount'] / total * 100, 2) for p in state['portfolio']}
    state['analysis'] = {"breakdown": breakdown}
    return state
