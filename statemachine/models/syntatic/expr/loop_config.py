loop_states = {
    "start": {
        "transitions": {"loop_expr": {"transition": "while"}},
        "initial_state": True,
    },
    "loop_expr": {
        "check": ".",
        "model": "expr",
        "transitions": {"loop": {"transition": "loop"}},
    },
    "loop": {"transitions": {"inside_expr": {"transition": ""}}},
    "inside_expr": {
        "check": ".",
        "model": "expr",
        "transitions": {"end": {"transition": "pool"}},
    },
    "end": {"final_state": True},
}
