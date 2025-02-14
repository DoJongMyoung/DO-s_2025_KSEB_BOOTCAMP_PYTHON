# def pbo(n):
#     n_list=[0 ,1]
#     for i in range(n+1):
#         n_list.append(n_list[i] + n_list[i + 1])
#
#     return n_list[n]
#
#
# number = int(input("보고 싶은 n번째 피보나치 숫자: "))
# print(pbo(number))

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

print(fibonacci_recursion(int(input())))