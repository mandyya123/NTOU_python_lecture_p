'''販賣機
可以投任意金錢或按q退幣
販賣的商品有柳橙汁10元、礦泉水15元、牛奶30元
(沒有利用Function) 是否可以購買的運算 並顯示餘額
'''
money = input('請投入現金(按q退出投幣):') #money的input可以接受任意金額
if money == 'q':
	print('退出投幣')
	exit() #結束整個程式	
else:
	print(f'投入的現金為:{money}')

products = [['柳橙汁','10'], ['礦泉水','15'], ['牛奶','30']]
print(f'販售的飲品與售價:')
for p in products: #一次取一個
	print(f'{p[0]}:{p[1]}') #每一次取出的元素的第0跟1個元素

num = input('請輸入數字選擇要購買的飲料(柳橙汁:1 、礦泉水:2 、牛奶:3, 退出:q):')
if str(num) == 'q':
	print('退出投幣')	
else:
	print(f'輸入的數字為:{num}')

	num = int(num)
	money = int(money)
	# while num <= 3:	#使用while是為了讓程式一直執行
	if num == 1:
		products[0][1] = int(products[0][1])
		if money >= products[0][1]:
			remain = money - products[0][1]
			print(f'購買了{products[0][0]}花了{products[0][1]}元，還剩{remain}元')
			print('謝謝光臨')
		else:
			need = products[0][1]- money
			print(f'投入的金額不足喔,還需要{need}元')
			print('謝謝光臨')
		exit()	

	elif num == 2:
		products[1][1] = int(products[1][1])
		if money >= products[1][1]:
			remain = money - products[1][1]
			print(f'購買了{products[1][0]}花了{products[1][1]}元，還剩{remain}元')
			print('謝謝光臨')
		else:
			need = products[1][1]- money
			print(f'投入的金額不足喔,還需要{need}元')	
			print('謝謝光臨')
		exit()	

	elif num == 3:
		products[2][1] = int(products[2][1])
		if money >= products[2][1]:
			remain = money - products[2][1]
			print(f'購買了{products[2][0]}花了{products[2][1]}元，還剩{remain}元')
			print('謝謝光臨')
		else:
			need = products[2][1]- money
			print(f'投入的金額不足喔,還需要{need}元')
			print('謝謝光臨')
		exit()
		