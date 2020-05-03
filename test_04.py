from day04 import check_num, find_all, check_num2


def test_check_num():
    assert check_num("111111") == True
    assert check_num("223450") == False
    assert check_num("123789") == False


def test_first_part():
    assert find_all(248345, 746315, check_num) == 1019


def test_check_num2():
    assert check_num2("112233") == True
    assert check_num2("123444") == False
    assert check_num2("111122") == True


def test_second_part():
    assert find_all(248345, 746315, check_num2) == 660
