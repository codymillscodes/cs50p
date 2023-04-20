def main():
    coins = [25, 10, 5]
    paid_in_full = False
    price = 50
    while not paid_in_full:
        money = input(f"Amount Due: {price}\nInsert Coin: ")
        if int(money) in coins:
            price = price - int(money)
        if price <= 0:
            paid_in_full = True

    print(f"Change Owed: {abs(price)}")

main()