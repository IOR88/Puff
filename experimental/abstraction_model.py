class ModelRepresentation:

    def extend_model(self):
        pass


class AbstractionModelClass:
    """
    The AbstractionModelClass should be capable of saving some abstraction data layer,
    it doesn't have to define it's location regarding other data layers, straight away.
    Sometimes I can be not possible to define location due to lack of some critical information
    about data layer.

    But AbstractionModelClass has to provide a way to change it's abstraction data layer into a
    real one with regards to whole data stream provided at any time. So it has to be flexible.
    """