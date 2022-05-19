assignment_states = {
    "id": {
        "check": r"\w+",
        "model": "id",
        "transitions": {"arrow": {"transition": "<-"}},
        "initial_state": True,
    },
    "arrow": {"transitions": {"expr": {"transition": ""}}},
    "expr": {
        "check": r"\w+",
        "model": "expr",
        "transitions": {"end": {"transition": ""}},
    },
    "end": {"final_state": True},
}
