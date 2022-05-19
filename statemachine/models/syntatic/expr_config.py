expr_states = {
    "start": {
        "transitions": {
            "loop": {"transition": ""},
            "conditional": {"transition": ""},
            "new": {"transition": ""},
            "isvoid": {"transition": ""},
            "case": {"transition": ""},
            "let": {"transition": ""},
            "assignment": {
                "transition": "",
            },
            "dispatch": {"transition": ""},
            "operation": {"transition": ""},
            "constant": {"transition": ""},
            "id": {"transition": ""},
        },
        "initial_state": True,
    },
    "isvoid": {
        "check": "isvoid .+",
        "model": "isvoid",
        "transitions": {"end": {"transition": ""}},
    },
    "operation": {
        "check": r"\w+ \+|\*|-|/ \w+",
        "model": "operation",
        "transitions": {"end": {"transition": ""}},
    },
    "new": {
        "check": "new .+",
        "model": "new",
        "transitions": {"end": {"transition": ""}},
    },
    "case": {
        "check": r"case .+ of ?.+;.+esac",
        "model": "case",
        "transitions": {"end": {"transition": ""}},
    },
    "let": {
        "check": r"let .+ : .+ in .+",
        "model": "let",
        "transitions": {"end": {"transition": ""}},
    },
    "loop": {
        "check": r"while .+ loop .+ pool",
        "model": "loop",
        "transitions": {"end": {"transition": ""}},
    },
    "dispatch": {
        "check": r"\w+\.\w+\(.*\)",
        "model": "dispatch",
        "transitions": {"end": {"transition": ""}},
    },
    "conditional": {
        "check": r"if .+ then .* fi",
        "model": "conditional",
        "transitions": {"end": {"transition": ""}},
    },
    "constant": {
        "check": r"(true|false|\d+(\.\d+)?|\".*\")",
        "model": "constant",
        "transitions": {"end": {"transition": ""}},
    },
    "assignment": {
        "check": r"\w+ ?<- ?\w+",
        "model": "assignment",
        "transitions": {"end": {"transition": ""}},
    },
    "id": {"check": r"\w+", "model": "id", "transitions": {"end": {"transition": ""}}},
    "end": {"final_state": True},
}
