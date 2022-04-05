class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice
        
    def getSymbol(self):
        return str(self.__symbol)

    def setSymbol(self, symbol):
        self.__symbol = symbol
    
    def getName(self):
        return str(self.__name)

    def setName(self, name):
        self.__name = name
    
    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice
    
    def setPreviousClosingPrice(self, PreviousClosingPrice):
        self.__previousClosingPrice = PreviousClosingPrice
        
    def getCurrentPrice(self):
        return self.__currentPrice
    
    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice
        
    def getChangePercent(self):
        var = self.__previousClosingPrice - self.__currentPrice
        var2 = var/self.__currentPrice
        var3 = var2 * 100
        return var3
