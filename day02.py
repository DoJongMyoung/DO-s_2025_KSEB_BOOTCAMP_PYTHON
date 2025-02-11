#dan = input("Input dan : ") #이리하면 오류발생
dan =  int(input("Input dan : "))
for i in range(1,10,1):
    print(f"{dan}*{i}={dan * i}")


# for dan in range(2, 10, 1): #python은 들여쓰기 중요함, 끝나는 숫자는 10-1인 9
#     for i in range(1, 10, 1):
#         print(f"{dan} * {i} = {dan * i}")
