# def fibonacci_loop(n) -> int:
#    """
#    피보나치 수 게산함수 (반복문 버전)
#    :param n:
#    :return:
#    """
#    n_list = [0, 1]
#    for i in range(n + 1):
#        n_list.append(n_list[i] + n_list[i + 1])
#
#    return n_list[n]
#
# number = int(input("loop ver 보고 싶은 n번째 피보나치 숫자: "))
# print(fibonacci_loop(number))
#
# def fibonacci_recursion(n) -> int:
#     """
#     재귀 함수를 이용한 피보나치 계산
#     :param n:
#     :return: int타입의 피보나치 값
#     """
#     if n<=0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)
#
# print(fibonacci_recursion(int(input("recursion 보고 싶은 n번째 피보나치 숫자: "))))


def bomb_recursion(num):
    if num < 0:
        return
    if num == 0:
        print("bomb!")
    else:
        print(num)
    return bomb_recursion(num-1)

time1 = int(input("recurion ver n초뒤 폭발 : "))
bomb_recursion(time1)

def bomb_loop(num):
    for i in range(num+1):
        if i != num:
            print(f"{num - i}초뒤 폭발 !")
        else:
            print("bomb!")

time2 = int(input("loop ver n초뒤 폭발 : "))
bomb_loop(time2)