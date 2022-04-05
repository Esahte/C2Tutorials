from time import time


class StopWatch:
    def __init__(self):
        self.__startTime = time()
        # self.__endTime = time()

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def start(self):
        self.__startTime = time()

    def stop(self):
        self.__endTime = time()

    def getElapsedTime(self):
        var = (self.__endTime - self.__startTime) * 1000
        return int(var)
