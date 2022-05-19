attr_states = {
    "var_name": {
        "check": r"\w+",
        "model": "id",
        "transitions": {"attr_type": {"transition": ":"}},
        "initial_state": True,
    },
    "attr_type": {
        "check": r"[A-Z]*",
        "model": "type",
        "transitions": {"arrow": {"transition": "<-"}, "comma": {"transition": ";"}},
    },
    "arrow": {
        "check": "<-",
        "model": "expr",
        "transitions": {"comma": {"transition": ";"}},
    },
    "comma": {"transitions": {}, "final_state": True},
}
