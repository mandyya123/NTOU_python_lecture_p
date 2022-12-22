#猜數字遊戲
import random
answer = random.randint(0,100) #random.randint(x,y)會產生一個x~y之間的隨機整數
times = 0 #可省略

level = input('請輸入難易度(Easy, Hard, God)大小寫要相同喔:')
level = level.capitalize() #將字串中的第一個字母大寫，其餘小寫;title():將每組單詞(空格區分)的第一個字母大寫，其餘小寫
#如何改善(輸入的大小寫與定義的不同)的問題? 解答如上
'''
if level == 'Easy':
	times = 15 #可以猜的次數(隨著遊戲難度不同而改變)
	print(f'遊戲難度為:{level} 可猜{times}次 \n 遊戲開始!')
elif level == 'Hard':
	times = 8
	print(f'遊戲難度為:{level} 可猜{times}次 \n 遊戲開始!')
elif level == 'God':
	times = 5
	print(f'遊戲難度為:{level} 可猜{times}次 \n 遊戲開始!')
else:
	print('請輸入Easy, Hard, God其中一個')
'''	
if level == 'Easy':
	times = 15 #可以猜的次數(隨著遊戲難度不同而改變)	
elif level == 'Hard':
	times = 8
elif level == 'God':
	times = 5
else:
	print('請輸入Easy, Hard, God其中一個')
print(f'遊戲難度為:{level} 可猜{times}次 \n 遊戲開始!')

while True:
	number = input('請輸入答案(範圍介於0~100之間):')
	number = int(number)
	times = times - 1
	if number < 0 or number > 100:	 #先判斷數值是否介於0~100
	 	print(f'數值超出範圍 \n 剩餘{times}次')
	if number < answer:
		print(f'大一點 \n 剩餘{times}次')
		if times <= 0:
			print(f'答案是{answer},遊戲結束')
			break
	elif number > answer:
		print(f'小一點 \n 剩餘{times}次')
		if times <= 0:
			print(f'答案是{answer},遊戲結束')
			break
	elif number == answer:
		print(f'猜對囉!答案是{answer}')
		break