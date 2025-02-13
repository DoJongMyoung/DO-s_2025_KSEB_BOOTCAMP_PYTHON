

def log_decorator(func): #decorator는 함수를 인자로 받고, OCP원칙에 따라 안에 함수가 wrapped 상태
    def wrapper(*args, **kWargs):
        print(f'Function Name : {func.__name__}')
        print(f'Function Arguments : {args}')
        print(f'Function Keyword Arguments : {kWargs}') # **kwargs는 딕셔너리 형태
        result = func(*args,**kWargs)
        return result
    return wrapper


@log_decorator
def greet(name, greeting="안녕하세요", age=None): #default인자 greeting은 따로 인자를 주지 않으면 안녕하세요가 출력, 아닌경우는 입력한 녀석 출력
    return f"{greeting}, {name} , (age = {age})" if age else f"{greeting}, {name}"
#나이를 입력 받지 않으면 (age 값이 0, None, False, 빈 문자열이면) 거짓으로 판단하여 if 조건문 앞에 있는 결과 출력
#아닌경우 else뒤 결과 출력


print(greet("인하"))
print(greet("종명","안녕"))
print(greet("James","Hello"))
print(greet("Gonzales",greeting = "Hola"))
print(greet("Nakamura",greeting = "Gonizizwa",age=29))

