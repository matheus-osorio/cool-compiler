class_states = {
    "class": {
        "transitions": {"class_name": {"transition": r"class"}},
        "initial_state": True,
    },
    "class_name": {
        "check": r"[a-z]\w*",
        "model": "type",
        "transitions": {
            "open_bracket": {"transition": r"{"},
            "inherits": {"transition": "inherits"},
        },
    },
    "inherits": {
        "check": "inherits",
        "model": "type",
        "transitions": {"open_bracket": {"transition": "{"}},
    },
    "open_bracket": {"transitions": {"close_bracket": {"transition": "}"}}},
    "close_bracket": {"transitions": {"comma": {"transition": ";"}}},
    "comma": {"transitions": {}, "final_state": True},
}
