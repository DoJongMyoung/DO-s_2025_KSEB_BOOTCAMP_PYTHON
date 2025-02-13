#SOLID
#open closed principle : 개방 폐쇄 원칙 (확장에는 열려있고 수정에는 닫혀있는 원칙)

#v3.6) 2중 데코레이터 적용, 성능측정 데코레이터, 디스크립션 데코레이터를 팩토리얼 함수에 적용하시오.
import time

def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f"실행시간 : {e - s}초")
        return r
    return wrapper

def des_decorator(f):  # closure
    def inner(*args):
        print(f"함수 이름 : {f.__name__}") #매직 키워드 : __기호있는 녀석들
        print(f"함수 설명 : {f.__doc__}") #실행되는 함수의 이름(__name__)과 설명(__doc__)을 출력함
        r = f(*args)
        return r

    return inner



@time_decorator #데코레이터를 주석처리함으로써 time_decorator를 사용 안함.
@des_decorator
def factorial_repetition(n) -> int:
    """팩토리얼 함수"""
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

number = int(input())
# ft = time_decorator(factorial_repetition) # 이름만 넣으면 주소를 호출 . 즉 time_decorator에 인수로 factorial_repetiton의 주소를 넣어줌.
print(f"{number}! = {factorial_repetition(number)}")

# number = int(input())
# print(f"{number}! = {factorial_repetition(number)}")

