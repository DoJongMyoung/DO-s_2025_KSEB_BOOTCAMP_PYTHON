def is_prime(num):
    i = 2
    if num >= 2:
        while i * i <= num :
            if num % i == 0:
                return False
            i = i + 1

    else:
        return False

    return True

n = int(input("Input number : "))

if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number!")