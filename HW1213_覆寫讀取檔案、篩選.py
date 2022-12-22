'''題目:讀取ex1.txt ，將50筆隨機整數(0,100)寫入ex1.txt中
統計ex1.txt中>50有幾個；再統計ex1.txt中有幾個偶數 並將{其中}偶數的數字列出來
'''
#要新增一個ex1.txt的檔案
import random
#先將會用到的清單列出來
numbers = []
over_fifty = []
even_num = []
#將隨機整數寫入ex01.txt中
with open('ex1.txt','w') as t:
	for num in range(50): #印出特定數量 一次一次取
		print(f'正在執行第{num+1}次') #顯示執行到第幾次
		num = random.randint(0,100) #要寫在for裡面 每次跑出來的number才會不同
		numbers.append(num)
		t.write(str(num) +'\n',) #txt文字檔輸入的內容只能是字串 
		#要用'+'不能用','; 也可以寫成: print(str(num), file = t)
		#統計ex1.txt中>50有幾個
		num = int(num) #將字串轉成整數型態做運算
		if num > 50 :
			over_fifty.append(num)
		#統計ex1.txt中有幾個偶數 並將偶數列出來	
		if num % 2 == 0 : #不能使用elif!!!因為是判斷兩個不同的條件
			even_num.append(num)
	print(over_fifty)	#要打在跟for的位置一樣(跳出if迴圈)
	print(f'共有{len(over_fifty)}個數字>50')		
	print(even_num)
	print(f'共有{len(even_num)}個偶數')

'''原始寫法
import random
number = []
count = 0
#將隨機整數寫入ex01.txt中
with open('ex1.txt','w') as t:
	for num in range(50): #印出特定數量
		count += 1
		print(f'正在執行第{count}次') #顯示執行到第幾次
		num = random.randint(0,100) #要寫在for裡面 每次跑出來的number才會不同
		number = str(num) #輸入的內容只能是字串，要將整數型態轉成字串
		t.write(number +'\n',) #要用'+'不能用','; 也可以寫成: print(num, file = t)

#統計ex1.txt中>50有幾個
over_fifty = []
with open('ex1.txt','r') as t:
	#over_fifty = [num for num in t if num > 50] #快寫法???
	for num in t:
		num = int(num) #將字串轉為數值
		if num > 50 :
			over_fifty.append(num)
	print(over_fifty)	#要打在跟for的位置一樣(跳出if迴圈)
	print(f'共有{len(over_fifty)}個數字>50')		

#統計ex1.txt中 並將{其中}偶數的數字列出來
even_num = []
with open('ex1.txt','r') as t: #這行一定要打2次嗎???
	# even_num = [num for num in t if num % 2 == 0] #快寫法???
	for num in t:
		num = int(num)
		if num % 2 == 0 :
			even_num.append(num)
	print(even_num) #要打在跟for的位置一樣
	print(len(even_num))
'''