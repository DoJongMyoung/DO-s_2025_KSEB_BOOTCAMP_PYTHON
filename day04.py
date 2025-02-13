#v3.8)  kwargs를 이용한 데코레이터 예제
from xmlrpc.client import WRAPPERS


def log_decorator(func): #decorator는 함수를 인자로 받고, OCP원칙에 따라 안에 함수가 wrapped 상태
    def wrapper(*args, **kWargs):
        print(f'Function Name : {func.__name__}')
        print(f'Function Arguments : {args}')
        print(f'Function Keyword Arguments : {kWargs}') # **kwargs는 딕셔너리 형태
        result = func(*args,**kWargs)
        return result
    return wrapper


@log_decorator
def greet(name, greeting="안녕하세요", age=0): #default인자 greeting은 따로 인자를 주지 않으면 안녕하세요가 출력, 아닌경우는 입력한 녀석 출력
    return f"{greeting}, {name}"


print(greet("인하"))
print(greet("종명","안녕"))
print(greet("James","Hello"))
print(greet("Gonzales",greeting = "Hola"))
print(greet("Nakamura",greeting = "Gonizizwa",age=29))

