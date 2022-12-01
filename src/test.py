from utils import isAValidCreditCard

def check(answer, creditCardNumber):
    
    result = isAValidCreditCard(creditCardNumber)
    if result == answer:
        return True
    else:
        return False


# 49927398716        | True          |
# | 49927398717        | False         |
# | 1234567812345678   | False         |
# | 1234567812345670   | True          |
# | 2222405343248877   | True          |
# | 2222990905257051  True          


def test_1():
    print(check(True,"49927398716"))


def test_2():
    print(check(False, "49927398717"))


def test_3():
    print(check(False, "1234567812345678"))


def test_4():
    print(check(True, "1234567812345670"))


def test_5():
    print(check(True, "2222405343248877"))


def test_6():
    print(check(True, "2222990905257051"))


def test_all():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()

test_all()