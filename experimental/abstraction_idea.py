class TapeClass:
    """
    Abstract: long tape with chars data
    """
    pass


class GearClass:
    """
    Abstract: A gear that switches states above tape
    """
    pass


"""
Abstract: A state function takes part in execution context on provided data
          depending on it state, it can: orientate, interpret, write, save, delete
"""


def orientate_state():
    pass


def interpret_state():
    pass


def write_state():
    pass


def save_state():
    pass


def delete_state():
    pass


class DataClass:
    """
    Abstract: A wardrobe for storing information from PuffMotor actions
    Info: Must be a shared entity among all PuffMotorClass instances(amount will depend on pc available CPU's)
    """
    pass


class TemporaryModelLayer:
    """
    Abstract: It is a temporary, real time snapshot of each PuffMotor work already done during run action
    Info: After PuffMotorClass has done it's run action, this class should be joined with globally shared
          DataClass.
    """
    pass


class PuffMotorClass:
    """
    Abstract: Squizzy Machine, complex tool, consist of (TapeClass, GearClass, states functions, DataClass,
                                                         TemporaryModelLayer)
    """
    pass