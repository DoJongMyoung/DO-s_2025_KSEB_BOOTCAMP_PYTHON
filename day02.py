#prime number check program
n = int(input("Input number : "))

is_prime = True

if n >= 2:
    for i in range (2 , n):
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