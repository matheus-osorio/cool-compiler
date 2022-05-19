constant_states = {
    "start": {
        "initial_state": True,
        "transitions": {"end": {"transition": r"(true|false|\d+(\.\d+)?|\".*\")"}},
    },
    "end": {"final_state": True},
}
