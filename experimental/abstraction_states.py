"""
states functions @args:
    @data char()
"""

ORIENTATE = {
    '{': (),
    '}': (),
    '[': (),
    ']': (),
    ',': (),
    '"': (),
    ':': ()
}


def orientate_state(data):
    command = ORIENTATE.get(data, None)
    if command:
        return True, command
    return False
# =================== #


INTERPRET = {}


def interpret_state():
    pass
# =================== #


WRITE = {}


def write_state():
    pass
# =================== #


SAVE = {}


def save_state():
    pass
# =================== #


DELETE = {}


def delete_state():
    pass
# =================== #