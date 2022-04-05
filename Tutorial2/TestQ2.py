from Q2 import Fan


def main():
    fan1 = Fan()
    fan1.setSpeed(3)
    fan1.setRadios(10)
    fan1.setColor('yellow')
    fan1.turnOn()

    fan2 = Fan()
    fan2.setSpeed(2)
    fan2.turnOff()

    print(fan1.getSpeed(), fan1.getRadios(), fan1.getColor())
    print(fan2.getSpeed(), fan2.getRadios(), fan2.getColor())


main()
