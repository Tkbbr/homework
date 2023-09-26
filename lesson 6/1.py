games = []
while 1 :
    game = input('Введите название игры: ')
    if game == '0': break
    elif game in games :
        print('Эта игра уже записаа')
    else: games.append(game)

print(sorted(games))