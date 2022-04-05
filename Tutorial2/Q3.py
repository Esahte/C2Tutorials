class Account:
    def __init__(self, Id=0, balance=100, annualInterestRate=0):
        self.__id = Id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def setId(self, Id):
        self.__id = Id

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate / 100) / 12

    def getMonthlyInterest(self):
        return ((self.__annualInterestRate / 100) / 12) * self.__balance

    def withdraw(self, withdraws):
        self.__balance -= withdraws

    def deposit(self, deposit):
        self.__balance += deposit
