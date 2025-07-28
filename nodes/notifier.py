def notifier(state):
    print("📤 Final Advice for", state["user_name"])
    print("📊 Breakdown:", state["analysis"]["breakdown"])
    print("⚠️ Risks:", state["analysis"]["risks"])
    print("💡 Recommendation:\n", state["recommendation"])
    return state
