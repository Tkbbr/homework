price = int(input('Сумма к оплате: '))
hour = int(input('Текущий час(8-22): '))

if hour == 10 or hour == 11 or hour == 12 :
    price = price / 2
elif hour == 20 or hour == 21 or hour == 22:
    price = price / 4

print(price)