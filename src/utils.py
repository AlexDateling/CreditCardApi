def isAValidCreditCard(cardNumber : str):
    TotalSum = 0
    cardNumberLength = len(cardNumber)
    parity = cardNumberLength%2
    # loop backwards through digits of the card
    for i in range(cardNumberLength-1,-1,-1):
        currentDigit = int(cardNumber[i])
        if (i + 1)%2 == parity:
            TotalSum = TotalSum + currentDigit
        elif currentDigit > 4:
            TotalSum = TotalSum + 2*currentDigit - 9
        else:
            TotalSum = TotalSum + 2*currentDigit

    return ((TotalSum%10) == 0)