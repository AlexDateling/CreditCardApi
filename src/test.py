from utils import is_valid_credit_card

def check(answer, creditCardNumber):
    result = is_valid_credit_card(creditCardNumber)
    assert answer == result


# 49927398716        | True          |
# | 49927398717        | False         |
# | 1234567812345678   | False         |
# | 1234567812345670   | True          |
# | 2222405343248877   | True          |
# | 2222990905257051  True

def test_1():
    check(True, "49927398716")


def test_2():
    check(False, "49927398717")


def test_3():
    check(False, "1234567812345678")


def test_4():
    check(True, "1234567812345670")


def test_5():
    check(True, "2222405343248877")


def test_6():
    check(True, "2222990905257051")


def test_all():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()


test_all()
