from Q3 import Account


def main():
    account = Account(1122, 20000, 4.5)
    account.withdraw(2500)
    account.deposit(3000)

    print(f'the id is {account.getId()}, the balance {account.getBalance()}, the monthly interest rate is '
          f'{account.getMonthlyInterestRate()}, and the monthly interest is {account.getMonthlyInterest()}')


main()
