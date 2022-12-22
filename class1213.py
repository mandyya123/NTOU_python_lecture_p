#list:清單 可用來裝任何型態的資料
#index索引值:由0開始

a = ['toyota','honda','tesla', 123, True] 
print(a)
print(a[1]) 
print(a[1:4]) 
a.append('audi') #為清單加東西,append只能用在清單上,不能用在字串上
print(a)
print(len(a))
print('audi' in a) #判斷XXX是否在list中，輸出的結果為布林值

#For Loop :把清單的東西一個一個拿出來
#for x in list
cars = ['toyota','honda','tesla']
for car in cars: #car是"暫時性"的變數!!!只會在for裡面使用
#將清單cars的東西逐一拿出來，每次拿出來的東西命名為car
	print(car) 

#字串也可以當清單
car ='tesla'
for c in car:
	print(c)

#讀取檔案練習 
with open('food.txt','r') as f: #r:read(讀取) w:write(覆寫) a:附加 f.truncate(0)刪除
	for line in f:
		print(line)

#strip:將多餘的空格、換行都清掉
data =[]
with open('food.txt','r') as f: #離開with會自動關閉
	for line in f:
		data.append(line.strip())
print(data)
