"""
states functions @args:
    @data char()
"""

ORIENTATE = {
    '{': (),
    '}': ()
}


def orientate_state(data):
    if ORIENTATE.get(data):
        return True
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