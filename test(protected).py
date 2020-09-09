class Protected:
    def __init__(self):
        self.__privateVar = 24
        self._protectedVar = 15

    def getPrivate(self):
        print(self.__privateVar)

    def getProtected(self):
        print(self._protectedVar)

    def setPrivate(self, private):
        self.__privateVar = private


obj = Protected()
obj.getProtected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
