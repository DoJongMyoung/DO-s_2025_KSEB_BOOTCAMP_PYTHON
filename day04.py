import random

def print_menu_total_price(n):
    global total_price
    print(f'{drinks[n]}에 어울리는 안주는 {foods[n]} 입니다')
    print(f'가격 : {prices[n]}')
    total_price = total_price + prices[n]

drinks = ["위스키", "와인", "소주", "고량주" ]
foods = ["초콜릿", "치즈", "삽겹살", "양꼬치"]
prices = [50000, 30000, 5000, 7500]


amounts = list()
for i in range(len(drinks)):
    amounts.append(0)


drinks.append("사케")
drinks.append("위스키")

prices.append(25000)
prices.append(35000)

foods.append("광어회")
foods.append("낙곱새")

total_price = 0
menu_list = '다음 술중에서 고르세요.\n'
for i in range(len(drinks)):
    menu_list = menu_list + f'{i + 1}) {drinks[i]} '

menu_list = menu_list + f'{len(drinks) +1}) 아무거나 {len(drinks) + 2}) 종료 : '


while True:
    menu = int(input(menu_list))

    if  1 <= menu <= len(drinks) :
        print_menu_total_price(menu - 1)

    elif menu == len(drinks) + 1 :
        random_index = random.randint(0, len(drinks) - 1 )
        print(f'{drinks[random_index]}에 어울리는 안주는 {foods[random_index]} 입니다')

    elif menu == len(drinks) + 2 :
        print(f'다음에 또 오세요')
        break
