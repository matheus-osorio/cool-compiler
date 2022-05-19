dispatch_states = {
    "start": {
        "check": ".",
        "model": "expr",
        "actions": {"exclude": "start.transitions.dispatch"},
        "transitions": {
            "dot": {
                "transition": r"\.",
            }
        },
        "initial_state": True,
    },
    "dot": {"transitions": {"id": {"transition": ""}}},
    "id": {
        "check": r"\w+",
        "model": "id",
        "transitions": {"open": {"transition": r"\("}},
    },
    "open": {
        "transitions": {"expr": {"transition": ""}, "close": {"transition": r"\)"}},
    },
    "expr": {
        "check": r"\w+",
        "model": "expr",
        "transitions": {"close": {"transition": r"\)"}, "colon": {"transition": ","}},
    },
    "colon": {"transitions": {"expr": {"transition": ""}}},
    "close": {"final_state": True},
}
