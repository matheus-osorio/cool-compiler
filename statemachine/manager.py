import re


class State:
    def __init__(
        self,
        name,
        transitions={},
        initial_state=False,
        final_state=False,
        check=None,
        model=None,
        actions={},
    ):
        self.name = name
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_state = final_state
        self.check = check
        self.model = model
        self.actions = actions

    def build(self, objs):
        obj = {}
        for key in self.transitions:
            target = objs[key]
            obj[key] = {
                "target": objs[key],
                "transition": self.transitions[key]["transition"],
            }

            if target.check:
                obj[key]["check"] = target.check

        self.transitions = obj

    def set_subqueries(self, objs):
        self.make_instance = objs

    def make_subquery(self, text):
        model_name = self.model
        model = self.make_instance[model_name](self.make_instance, self.actions)
        pattern = model.run(text)

        if pattern:
            return pattern

        return None

    def run(self, text):
        full_pattern = ""
        if self.check:
            pattern = self.make_subquery(text)
            if not pattern:
                return None

            full_pattern += pattern
            text = text[len(full_pattern) :]

        for key in self.transitions:
            transition = self.transitions[key]

            if "check" in transition:
                if not re.search(r"^[ \n]*" + transition["check"], text):
                    continue
            search = re.search(r"^[ \n]*" + transition["transition"], text)

            if not search:
                continue

            pattern = search.group()
            full_pattern += pattern
            text_left = text[len(pattern) :]
            return (transition["target"], text_left, full_pattern)

        if self.final_state:
            return True

        return None


class StateManager:
    def __init__(self, configs):
        self.configs = configs
        self.transitions = self.make_transitions()

    def make_transitions(self):
        state_list = {}
        for key in self.configs:
            state_list[key] = State(key, **self.configs[key])

        self.state_list = state_list

        self.start = list(filter(lambda x: x.initial_state, state_list.values()))[0]

        for key in state_list:
            state = state_list[key]
            state.build(state_list)

        return state_list

    def set_subqueries(self, subqueries):
        for state in self.state_list.values():
            state.set_subqueries(subqueries)

    def run(self, text):
        state = self.start

        result = state.run(text)

        text_found = ""

        if not result:
            return None

        while result:
            if result == True:
                return text_found

            state, text, pattern = result
            text_found += pattern

            result = state.run(text)

        return None
