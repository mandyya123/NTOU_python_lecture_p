#註解:(ctrl + /)
#單引號跟雙引號的意義相同
#命令提示字元: python C:\Users\mandy\OneDrive\桌面\python\test01.py
#再命令提示字元中按方向鍵_上可以重覆上一個命令
#ctrl+c:強迫關掉程式

print("123") 
print("abc")
x = 4 
y = 3.0
x = 5
print(x)
print(y)

price = 10
pen = 0.38
rain = True
name = "Mandy"
print(price)
print(price,pen,rain,name) #可用逗號或加號分隔每一個變數 逗點代表一個空格
print(type(price)) #顯示變數的資料型態(整數、浮點數、布林值、字串)
print(type(pen))
print(type(rain))
print(type(name))

a = 1 #只有print 數字可以不用引號
b = 'aabb'
print('aaabbb')
print('aaa','bbb')
name = 'Mandy'
print('www',name,'com',sep = '.') #間格變成.

#導入時間模組
import time
print("---Loading Example---")
print("Loading",end = "")
for i in range(20):
    print(".",end = '',flush = True) #flush:使程式重新整理/執行
    time.sleep(0.5) #每0.5秒產生一個點

name01 = input("\n"+"請輸入你的名字:")
print(name01, "你好")

#f是前綴詞 大括號的內容(變數名稱)是要替換的內容(變數的內容)
classes = '運輸碩一'
name = 'Mandy'
mail = 'mandyya1999123@gmail.com'
print(f"\n 個人資料\n 班級:{classes}\n 姓名:{name} \n Email:{mail}")
#同上式 print("個人資料"+"\n"+"班級:"+classes+"\n"+"姓名:"+name+"\n"+"Email:"+mail)

#print(f"\
	#個人資料\n\
	#班級:{classes}\n\
	#姓名:{name} \n\
	#Email:{mail}")


