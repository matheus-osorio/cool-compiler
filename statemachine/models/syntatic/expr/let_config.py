let_states = {
    "start": {
        "initial_state": True,
        "transitions": {
            "id": {"transition": "let"},
        },
    },
    "id": {"check": ".", "model": "id", "transitions": {"colon": {"transition": ":"}}},
    "colon": {"transitions": {"type": {"transition": ""}}},
    "type": {
        "check": ".",
        "model": "type",
        "transitions": {
            "in": {"transition": "in"},
            "comma": {"transition": ","},
            "arrow": {"transition": "<-"},
        },
    },
    "comma": {"transitions": {"id": {"transition": ""}}},
    "arrow": {"transitions": {"expr": {"transition": ""}}},
    "expr": {
        "check": ".",
        "model": "expr",
        "transitions": {"comma": {"transition": ","}, "in": {"transition": "in"}},
    },
    "in": {"transitions": {"final_expr": {"transition": ""}}},
    "final_expr": {
        "check": ".",
        "model": "expr",
        "transitions": {"end": {"transition": ""}},
    },
    "end": {"final_state": True},
}
