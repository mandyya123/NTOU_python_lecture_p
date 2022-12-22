#二維清單

#確認檔案在不在os
import os #作業系統os可以用來找檔案
if os.path.isfile('product.csv'):
	print('找得到檔案!')
else:
	print('找不到檔案!')

#讓使用者輸入
product = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價錢:')
	# p = []
	# p.append(name)
	# p.append(price)
	p = [name, price] #取代上面三行
	product.append(p)
print(f'Product是{product}')	

#顯示商品對應價格
for p in product:
	print(f'{p[0]}的價格是:{p[1]}')

#寫入檔案 (命令提示字元執行的資料夾為檔案位置)
with open('product.csv','w') as f: #若有亂碼可在'w'後面加encoding = 'utf-8'
	f.write('產品,價格\n') #寫入標題 ,是csv裡面的分隔符號
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n') #寫入

#讀取檔案
with open('product.csv','r') as f:
	for line in f:
		if '產品,價格' in line:
			continue #繼續執行for迴圈
		name, price = line.strip().split(',')
		product.append([name, price])
print(f'product是{product}')


#function:用來收納程式碼(只是功能不會執行)
def wash(dry): #括號內為參數，如果有參數一定會執行
	print('加水')
	print('加洗衣精')
	print('開始洗衣服')
	if dry:
		print('烘衣')
wash(True) #會出現if條件成立的結果
wash(False)

#function回傳值
def add(x, y):#x y為暫時變數
	return x + y
result = add(2,4) 
print(result)

#計算清單的平均數
def average(numbers):
	return sum(numbers)/len(numbers)
print(average([1,2,3])) #數值要用中括號


