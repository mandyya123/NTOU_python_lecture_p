'''販賣機
可以投15、50、100元或按q退幣
販賣的商品有柳橙汁10元、礦泉水15元、牛奶30元
利用Function進行 是否可以購買的運算 並顯示餘額
'''
def buy(products, price, money):	
	if money >= price:
		remain = money - price
		print(f'購買了{products}花了{price}元，還剩{remain}元')
	else:
		need = price - money
		print(f'投入的金額不足喔,還需要{need}元')

money = input('請投入現金只限15、50、100元，按q退出投幣:')
if money == 'q':
	print('退出投幣')
	exit() #結束整個程式	
elif money == "15" or money == "50" or money == "100":
	print(f'投入的現金為:{money}元')
else:
	print(f'請投入現金15、50、100元，按q退出投幣')
	exit()

print('飲料&售價: 柳橙汁 10元, 礦泉水 15元, 牛奶 30元')
num = input('請輸入數字選擇要購買的飲料(柳橙汁:1 、礦泉水:2 、牛奶:3, 退出:q):')

if num =='q':
	exit()
elif num == '1':
	buy('柳橙汁', 10, int(money))
elif num == '2':
	buy('礦泉水', 15, int(money))
elif num == '3':
	buy('牛奶', 30, int(money))		
else:
	print('請輸入要求的數字或q離開')

print('謝謝光臨')

