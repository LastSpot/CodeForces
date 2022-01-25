number_of_shops = int(input())
bottles_prices = sorted(list(map(int, input().split())))
days_of_drinking = int(input())
for i in range(days_of_drinking):
    shop_purchase = 0
    number_of_coins = int(input())
    for n in range(len(bottles_prices)):
        price_of_bottle = bottles_prices[n]
        if price_of_bottle <= number_of_coins:
            shop_purchase += 1
    print(shop_purchase)