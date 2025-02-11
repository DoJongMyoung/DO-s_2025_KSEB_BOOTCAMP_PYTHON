#prime number check program
#import math

n = int(input("Input number : "))
#print(int(15**0.5))

is_prime = True
i = 2
if n >= 2:
    for i in range (2,int(n**0.5)+1): #소수가 아니면 짝을 이루므로 제곱근과 비교해도 괜찮음.
        if n % i == 0 :
            is_prime = False
            break
            #print(i , end=' ') #몇번 실행되는지 확인하는 코드
else:
     is_prime = False

if is_prime:
    print(f"{n} is prime number")
else :
    print(f"{n} is not prime number")