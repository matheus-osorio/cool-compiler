case_states = {
    "start": {
        "initial_state": True,
        "transitions": {"initial_expr": {"transition": "case"}},
    },
    "initial_expr": {
        "check": r".",
        "model": "expr",
        "transitions": {"id": {"transition": "of"}},
    },
    "id": {
        "check": ".",
        "model": "id",
        "transitions": {"comma": {"transition": ":"}},
    },
    "comma": {"transitions": {"type": {"transition": ""}}},
    "type": {
        "check": ".",
        "model": "type",
        "transitions": {"arrow": {"transition": "=>"}},
    },
    "arrow": {"transitions": {"expr": {"transition": ""}}},
    "expr": {
        "check": ".",
        "model": "expr",
        "transitions": {"semicolon": {"transition": ";"}},
    },
    "semicolon": {
        "transitions": {"end": {"transition": "esac"}, "id": {"transition": ""}}
    },
    "end": {"final_state": True},
}
