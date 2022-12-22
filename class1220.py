#refactor:程式重構:全部改成function
#確認檔案在不在
import os
#讀取檔案
def read_file(filename):
	products = [] #products清單要放在迴圈外
	if os.path.isfile(filename): #相對路徑 絕對路徑
		print('找到檔案了!')
		with open(filename, 'r', encoding = 'utf-8') as f:
			for line in f:
				if '產品,價格' in line:
					continue #繼續
				name, price = line.strip().split(',')  #拿什麼當作切割的標準
				products.append([name,price])
		print(f"products是{products}")
	else:
		print('檔案不存在!')
	return products #回傳主程式需要的值

#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		products.append([name, price])
	print("products是:",products)
	return products

#顯示所有購買紀錄
def print_product(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename,products):
	with open(filename, 'w', encoding = 'utf-8') as f: #打開檔案
		f.write('產品,價格\n')
		for p in products:
			f.write(str(p[0]) + ',' + str(p[1]) + '\n') #寫入

#創建新檔案
def write_newfile(filename):
	products = []
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		products.append([name, price])
	print("products是:",products) 
	with open(filename, 'w', encoding = 'utf-8') as f: #打開檔案
		f.write('產品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') #寫入

#初始化文件(檔案才會清空，書寫一個全新的檔案)	
def initialize_file(filename):
	with open(filename, 'w', encoding = 'utf-8') as f: #打開檔案
		f.write('產品,價格\n')


#執行 main function
def main():
	write_newfile('products.csv')
	initialize_file('products.csv')
	products = read_file('products.csv')
	products = user_input(products)
	print_product(products)
	write_file('products.csv',products)

main()
