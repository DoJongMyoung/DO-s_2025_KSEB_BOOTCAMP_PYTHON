#dic을 빼고 list로만 동작되게 만들어라 .

import random

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

while True:
    menu = input(f'다음 술중에 고르세요.\n1) {drinks[0]}   2) {drinks[1]}   3) {drinks[2]}   4) {drinks[3]}   5) {drinks[4]}  6) {drinks[5]}   7) 아무거나   8) 종료 : ')
    if menu == '1':
        print(f'{drinks[0]}에 어울리는 안주는 {foods[0]} 입니다')
    elif menu == '2':
        print(f'{drinks[1]}에 어울리는 안주는 {foods[1]} 입니다')
    elif menu == '3':
        print(f'{drinks[2]}에 어울리는 안주는 {foods[2]} 입니다')
    elif menu == '4':
        print(f'{drinks[3]}에 어울리는 안주는 {foods[3]} 입니다')
    elif menu == '5':
        print(f'{drinks[4]}에 어울리는 안주는 {foods[4]} 입니다')
    elif menu == '6':
        print(f'{drinks[5]}에 어울리는 안주는 {foods[5]} 입니다')
    elif menu == '7':
        random_index = random.randint(0,5)
        print(f'{drinks[random_index]}에 어울리는 안주는 {foods[random_index]} 입니다')
    elif menu == '8':
        print(f'다음에 또 오세요')
        break