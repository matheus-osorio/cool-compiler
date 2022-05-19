method_states = {
    "func_id": {
        "model": "id",
        "check": r"\w+",
        "transitions": {"open": {"transition": r"\("}},
        "initial_state": True,
    },
    "open": {
        "transitions": {
            "func_params": {"transition": ""},
            "close": {"transition": r"\)"},
        }
    },
    "func_params": {
        "check": r"\w+",
        "model": "id",
        "transitions": {"type_part": {"transition": ":"}},
    },
    "type_part": {
        "check": r": ?\w+",
        "model": "type",
        "transitions": {
            "comma": {"transition": ","},
            "close": {"transition": r"\)"},
        },
    },
    "comma": {"transitions": {"func_params": {"transition": ""}}},
    "close": {"transitions": {"colon": {"transition": ":"}}},
    "colon": {
        "check": ":",
        "model": "type",
        "transitions": {"open_bracket": {"transition": r"\{"}},
    },
    "open_bracket": {
        "transitions": {
            "close_bracket": {"transition": "}"},
            "expr": {"transition": ""},
        }
    },
    "close_bracket": {"transitions": {"semicolon": {"transition": ";"}}},
    "expr": {
        "check": r"\w+",
        "transitions": {
            "close_bracket": {"transition": "}"},
            "expr": {"transition": ""},
        },
    },
    "semicolon": {"transitions": {}, "final_state": True},
}
