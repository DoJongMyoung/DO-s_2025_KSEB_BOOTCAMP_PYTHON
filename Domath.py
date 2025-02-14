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

def fibonacci_loop(n):
    n_list=[0 ,1]
    for i in range(n+1):
        n_list.append(n_list[i] + n_list[i + 1])

    return n_list[n]


# number = int(input("보고 싶은 n번째 피보나치 숫자: "))
# print(fibonacci_loop(number))

def fibonacci_recursion(n) -> int:
    """
    재귀 함수를 이용한 피보나치 계산
    :param n:
    :return: int타입의 피보나치 값
    """
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)

# print(fibonacci_recursion(int(input())))