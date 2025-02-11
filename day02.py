def my_pow(b,e) -> float:
    """
A user-defined function that receives a base and exponent and returns the power result in the form of a real number    :param b:
    :param b: base number
    :param e: exponnent
    :return: the power result in the form of a real number
    """
    result = 1
    for k in range(e):
        result = result * b
    return result


def is_prime(num) -> bool:
    if num >= 2:
        i = 2
       # while i < (int(my_pow(num, 0.5)) + 1):
        while i * i < num+1 :
            if num % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True

numbers = input("Input number : ").split()  # ex) 900 1000
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

j = n1
while j <= n2:
    if is_prime(j):
        print(j, end=' ')
    j = j + 1
