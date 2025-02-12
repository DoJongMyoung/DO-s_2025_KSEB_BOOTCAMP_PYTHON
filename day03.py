# #메뉴 삭제 추가에 대응되는 코드를 추가하라
#
# import random
#
# drinks = ["위스키", "와인", "소주", "고량주" ]
# foods = ["초콜릿", "치즈", "삽겹살", "양꼬치"]
#
# # print(drinks_foods)
# # print(drinks_foods.pop("고량주"))
# # print(drinks_foods)
#
# #del drinks_foods["위스키"]
# #drinks_foods["사케"] = "광어회"
# # drinks.append("사케")
# # drinks.append("위스키")
#
# foods.append("광어회")
# foods.append("낙곱새")
# #drink = input(drinks_foods.keys())
# #drinks_foods_keys = list(drinks_foods)
# # print(drinks_foods_keys)
# # #print(drinks_foods_keys.pop(0))
# # print(drinks_foods_keys.remove("위스키"))
# # print(drinks_foods_keys)
# #print(random.choice(drinks_foods_keys))
#
# def catch_num() -> int:
#     num = int(input("숫자를 입력하세요 : "))
#
#     return num
#
# menu_list = '다음 술중에서 고르세요.\n'
# for i in range(len(drinks)):
#     menu_list = menu_list + f'1) {drinks[i]} '
#
# print(menu_list)
#
#
# while True:
#     # menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}  6) {drinks[5]}   7) 아무거나   8) 종료 : ')
#     # for i in range(0, len(drinks) , 1):
#     #     print(f'{i + 1}) {drinks[i]}')
#
#     menu = input(menu_list)
#
#     number = catch_num()
#
#     if number >= 1 and number <= len(drinks) :
#         print(f'{drinks[number - 1]}에 어울리는 안주는 {foods[number - 1]} 입니다')
#     # if menu == '1':
#     #     print(f'{drinks[0]}에 어울리는 안주는 {foods[0]} 입니다')
#     # elif menu == '2':
#     #     print(f'{drinks[1]}에 어울리는 안주는 {foods[1]} 입니다')
#     # elif menu == '3':
#     #     print(f'{drinks[2]}에 어울리는 안주는 {foods[2]} 입니다')
#     # elif menu == '4':
#     #     print(f'{drinks[3]}에 어울리는 안주는 {foods[3]} 입니다')
#     # elif menu == '5':
#     #     print(f'{drinks[4]}에 어울리는 안주는 {foods[4]} 입니다')
#     # elif menu == '6':
#     #     print(f'{drinks[5]}에 어울리는 안주는 {foods[5]} 입니다')
#     elif number == 7 :
#         random_index = random.randint(0,len(drinks) - 1)
#         print(f'{drinks[random_index]}에 어울리는 안주는 {foods[random_index]} 입니다')
#     elif number == 8 :
#         print(f'다음에 또 오세요')
#         break
#while 안쪽의 하드 코딩된 코드를 함수화 하시오
import random

def print_menu(n):
    print(f'{drinks[n]}에 어울리는 안주는 {foods[n]} 입니다')


drinks = ["위스키", "와인", "소주", "고량주" ]
foods = ["초콜릿", "치즈", "삽겹살", "양꼬치"]

# print(drinks_foods)
# print(drinks_foods.pop("고량주"))
# print(drinks_foods)

#del drinks_foods["위스키"]
#drinks_foods["사케"] = "광어회"
drinks.append("사케")
drinks.append("위스키")

foods.append("광어회")
foods.append("낙곱새")
#drink = input(drinks_foods.keys())
#drinks_foods_keys = list(drinks_foods)
# print(drinks_foods_keys)
# #print(drinks_foods_keys.pop(0))
# print(drinks_foods_keys.remove("위스키"))
# print(drinks_foods_keys)
#print(random.choice(drinks_foods_keys))

menu_list = '다음 술중에서 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i + 1}) {drinks[i]} '

menu_list = menu_list + f'{len(drinks) +1}) 아무거나 {len(drinks) + 2}) 종료 : '


while True:
    menu = int(input(menu_list))

    if  1 <= menu <= len(drinks) :
        print_menu(menu - 1)

    elif menu == len(drinks) + 1 :
        random_index = random.randint(0, len(drinks) - 1 )
        print(f'{drinks[random_index]}에 어울리는 안주는 {foods[random_index]} 입니다')

    elif menu == len(drinks) + 2 :
        print(f'다음에 또 오세요')
        break