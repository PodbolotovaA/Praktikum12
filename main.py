per_cent = {'tk': 5.6, 'sk': 5.9, 'vt': 4.28, 'sb': 4.0}
money = int(input('Введите сумму, которую планируете положить под проценты '))
deposit1=money*per_cent['tk']/100
deposit2=money*per_cent['sk']/100
deposit3=money*per_cent['vt']/100
deposit4=money*per_cent['sb']/100
deposit =[]
deposit.append(deposit1)
deposit.append(deposit2)
deposit.append(deposit3)
deposit.append(deposit4)
print('Максимальная сумма, которую вы можете заработать -',(max(deposit)))