# This program implements a deque in Python


class Deque:
    """
    This class contains attributes of a deque.
    """

    def __init__(self, elements=[]):
        # type: (list) -> None
        self.elements: list = elements

    def append(self, element):
        # type: (object) -> None
        self.elements.append(element)

    def append_left(self, element):
        # type: (object) -> None
        self.elements.insert(0, element)

    def pop(self):
        # type: () -> object
        to_be_returned: object = self.elements[len(self.elements) - 1]
        self.elements.remove(to_be_returned)
        return to_be_returned

    def pop_left(self):
        # type: () -> object
        to_be_returned: object = self.elements[0]
        self.elements.remove(to_be_returned)
        return to_be_returned

    def __str__(self):
        # type: () -> str
        return str(self.elements)


a: Deque = Deque()
a.append(5)
a.append_left(7)
print(a)
a.append_left(4)
a.append(6)
print(a)
print(a.pop_left())
print(a)
print(a.pop())
print(a)
