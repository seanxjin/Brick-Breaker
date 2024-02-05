class ParentClass:

    def __init__(self):
        self.__private_attributes = 1
        self._partially_protected_attribute = 2
        self.public_attribute = 3

    def __private_method(self):
        return 4

    def _partially_protected_method(self):
        return 5

    def public_method(self):
        return 6

    def getPartiallyProtectedAttribute(self):
        return self._partially_protected_attribute

    def getProtectedAttribute(self):
        return self.__private_attributes


class Subclass(ParentClass):

    def __init__(self):
        ParentClass.__init__(self)
        self.__private_attributes = 7  # different attribute than the parent
        self._partially_protected_attribute = 8
        self.public_attribute = 9


MY_CLASS = Subclass()
print(MY_CLASS.getPartiallyProtectedAttribute())
print(MY_CLASS.getProtectedAttribute())  # 1