class Fan:
    def __init__(self):
        self.__speed = 1
        self.__on = False
        self.__radius = 5
        self.__color = 'blue'

    def turnOn(self):
        self.__on = True

    def turnOff(self):
        self.__on = False

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed

    def getRadios(self):
        return self.__radius

    def setRadios(self, radius):
        self.__radius = radius


# def main():
#     fan1 = Fan()
#     fan1.setSpeed(3)
#     fan1.setRadios(10)
#     fan1.setColor('yellow')
#     fan1.turnOn()
#
#     fan2 = Fan()
#     fan2.setSpeed(2)
#     fan2.turnOff()
#
#     print(fan1.getSpeed(), fan1.getRadios(), fan1.getColor())
#     print(fan2.getSpeed(), fan2.getRadios(), fan2.getColor())
#
#
# main()
