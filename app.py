from json import dumps, loads

from statemachine.manager import StateManager

# from statemachine.models.lexic import configs
from statemachine.models.syntatic import configs


def call(model):
    def wrapper(model_list, actions={}):
        nonlocal model
        usable = model
        for action_name in actions:
            action = actions[action_name]
            usable = loads(dumps(usable))
            if action_name == "exclude":
                path = action.split(".")
                final = path[-1]
                path = path[:-1]
                entry = usable
                for name in path:
                    entry = entry[name]
                del entry[final]

        manager = StateManager(usable)
        manager.set_subqueries(model_list)
        return manager

    return wrapper


subqueries = {}
for name in configs["models"]:
    model = configs["models"][name]
    subqueries[name] = call(model)

proximity = 10000
saved_name = None
saved = ""

for name in subqueries:
    maker = subqueries[name]
    model = maker(subqueries)
    text = r"""class Name inherits Type { test : Test; };"""
    response = model.run(text)
    if not response:
        continue
    if abs(len(response) - len(text)) < proximity:
        saved_name = name
        saved = response
        proximity = abs(len(response) - len(text))


print({"proximity": proximity, "name": saved_name, "pattern": saved})
