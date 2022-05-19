operation_states = {
    "start": {
        "check": ".",
        "model": "expr",
        "actions": {"exclude": "start.transitions.operation"},
        "initial_state": {"transitions": {"transition": r"\+-\*/"}},
    },
    "op": {"transitions": {"expr": {"transition": ""}}},
    "expr": {"check": ".", "model": "expr", "transitions": {"end": {"transition": ""}}},
    "end": {"final_state": True},
}
