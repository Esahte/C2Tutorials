from Q4 import Stock


def main():
    stk = Stock('UWEEFIC', 'The UWI Five Islands', 20.5, 20.35)

    print(f'the symbol is {stk.getSymbol()}, and the name is {stk.getName()}. the previous closing price was '
          f'{stk.getPreviousClosingPrice()}, the new closing price is {stk.getCurrentPrice()}, '
          f'and the price change percentage is {stk.getChangePercent()}')


main()
