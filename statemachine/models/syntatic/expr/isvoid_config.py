isvoid_states = {
    "start": {"initial_state": True, "transitions": {"expr": {"transition": "isvoid"}}},
    "expr": {"check": ".", "model": "expr", "transitions": {"end": {"transition": ""}}},
    "end": {"final_state": True},
}
