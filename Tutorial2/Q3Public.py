class Account:
    def __init__(self, Id=0, balance=100, annualInterestRate=0):
        self.id = Id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def getMonthlyInterestRate(self):
        return (self.annualInterestRate / 100) / 12

    def getMonthlyInterest(self):
        return ((self.annualInterestRate / 100) / 12) * self.balance

    def withdraw(self, withdraws):
        self.balance -= withdraws

    def deposit(self, deposit):
        self.balance += deposit