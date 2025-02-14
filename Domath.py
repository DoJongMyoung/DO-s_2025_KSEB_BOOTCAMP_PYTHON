def my_abs(n) -> int :
    """
    Return absolute value of parameter n
    :param n:
    :return:
    """
    if n < 0 :
        return -n
    return n # n이 음수가 아닌경우 그대로 출력

# print(my_abs(87),my_abs(-77))