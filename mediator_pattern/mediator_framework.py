class InteractiveObject:
    """進行交流的物件"""
    pass


class InteractiveObjectImplA:
    """實現類別A"""
    pass


class InteractiveObjectImplB:
    """實現類別B"""
    pass


class Mediator:
    """仲介類別"""
    def __init__(self):
        self._interactive_object_ImplA = InteractiveObjectImplA()
        self._interactive_object_ImplB = InteractiveObjectImplB()

    def interactive(self):
        """進行交流的操作"""
        pass

