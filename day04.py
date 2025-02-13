#SOLID
#open closed principle : 개방 폐쇄 원칙 (확장에는 열려있고 수정에는 닫혀있는 원칙)
import time

def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f"실행시간 : {e - s}초")
        return r
    return wrapper

# @time_decorator #데코레이터를 주석처리함으로써 time_decorator를 사용 안함.
def factorial_repetition(n) -> int:
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

number = int(input())
ft = time_decorator(factorial_repetition) # 이름만 넣으면 주소를 호출 . 즉 time_decorator에 인수로 factorial_repetiton의 주소를 넣어줌.
print(f"{number}! = {ft(number)}")

number = int(input())
print(f"{number}! = {factorial_repetition(number)}")

