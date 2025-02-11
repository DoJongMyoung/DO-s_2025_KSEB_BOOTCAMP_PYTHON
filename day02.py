#prime number check program
n = int(input("Input number : "))

is_prime = True

if n >= 2:
    count = 0
    for i in range (2 , n):
        if n % i == 0 :
            is_prime = False
            break
else:
     is_prime = False

if is_prime:
    print(f"{n} is prime number")
else :
    print(f"{n} is not prime number")