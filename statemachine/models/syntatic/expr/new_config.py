new_states = {
    "start": {"transitions": {"type": {"transition": "new"}}, "initial_state": True},
    "type": {"check": ".", "model": "type", "transitions": {"end": {"transition": ""}}},
    "end": {"final_state": True},
}
