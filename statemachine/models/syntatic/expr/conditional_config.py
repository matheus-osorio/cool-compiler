conditional_states = {
    "start": {"initial_state": True, "transitions": {"if_expr": {"transition": "if"}}},
    "if_expr": {
        "check": ".",
        "model": "expr",
        "transitions": {"if_then": {"transition": "then"}},
    },
    "if_then": {"transitions": {"inside_expr": {"transition": ""}}},
    "inside_expr": {
        "check": ".",
        "model": "expr",
        "transitions": {
            "end": {"transition": "fi"},
            "else": {"transition": "else"},
            "inside_expr": {"transition": ""},
        },
    },
    "else": {"transitions": {"else_expr": {"transition": ""}}},
    "else_expr": {
        "check": ".",
        "transitions": {"end": {"transition": "fi"}, "else_expr": {"transition": ""}},
    },
    "end": {"final_state": True},
}
