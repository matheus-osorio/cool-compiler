configs = {
    "code": {
        "model_name": "lexic_analyser",
        "transitions": {
            "text": {"transition": r'"'},
            "code": {"transition": r"."},
        },
        "initial_state": True,
        "final_state": True,
    },
    "text": {
        "transitions": {
            "code": {"transition": r'"'},
            "escaped": {"transition": r"\\"},
            "text": {"transition": r"."},
        }
    },
    "escaped": {"transitions": {"text": {"transition": r"."}}},
}
