hour = int(input('Текущий час(8-22): '))

cheqe = []
while 1 :
    price = int(input('Цена товара: '))
    if price == 0:
        break
    else:
        cheqe.append(price)

if cheqe[0] > cheqe[1] > cheqe[2]:
    print('Акция!')
    Resoult = sum(cheqe) / 2

elif cheqe[0] < cheqe[1] < cheqe[2]:
    print('Акция!')
    Resoult = sum(cheqe) / 3

if hour == 10 or hour == 11 or hour == 12 :
    Resoult = Resoult / 2
elif hour == 20 or hour == 21 or hour == 22:
    Resoult = Resoult / 4

print('К оплате:', Resoult)