# pylint: disable=import-error

from statemachine.models.syntatic.attr_config import attr_states
from statemachine.models.syntatic.class_config import class_states
from statemachine.models.syntatic.expr.assignment_config import assignment_states
from statemachine.models.syntatic.expr.case_config import case_states
from statemachine.models.syntatic.expr.conditional_config import conditional_states
from statemachine.models.syntatic.expr.constant_config import constant_states
from statemachine.models.syntatic.expr.dispatch_config import dispatch_states
from statemachine.models.syntatic.expr.isvoid_config import isvoid_states
from statemachine.models.syntatic.expr.let_config import let_states
from statemachine.models.syntatic.expr.loop_config import loop_states
from statemachine.models.syntatic.expr.new_config import new_states
from statemachine.models.syntatic.expr.operation_config import operation_states
from statemachine.models.syntatic.expr_config import expr_states
from statemachine.models.syntatic.id_config import id_states
from statemachine.models.syntatic.method_config import method_states
from statemachine.models.syntatic.type_config import type_states

configs = {
    "models": {
        "class": class_states,
        "attr": attr_states,
        "type": type_states,
        "id": id_states,
        "method": method_states,
        "expr": expr_states,
        "constant": constant_states,
        "assignment": assignment_states,
        "dispatch": dispatch_states,
        "conditional": conditional_states,
        "loop": loop_states,
        "let": let_states,
        "case": case_states,
        "new": new_states,
        "isvoid": isvoid_states,
        "operation": operation_states,
    },
}
