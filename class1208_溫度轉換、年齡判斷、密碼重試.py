#命令提示字元: python C:\Users\mandy\OneDrive\桌面\python\class1208.py

#比較運算式
x = 5 #給x一個值
x == 5 #判斷x是否等於5
x != 5
x <= 5
x >= 5
x < 5
x > 5    
print(x == 5) #結果為布林值(True、False)
print(x != 5)

#if
rain = input('請問今天有沒有下雨?')
if rain == '有':
	print('記得帶傘出門')

#if-elif-else
age = input('請輸入年齡:')
age = int(age) 
if age >= 20:
	print('可以投票')
else:
	print('還不能投票喔!')	

#溫度轉換程式(攝氏轉華氏)
temp_c = input('請輸入攝氏溫度:')
temp_c = float(temp_c)
f = temp_c * 9 / 5 + 32 
print('華氏溫度為:',f)
#也可以寫成 print(f'華氏溫度為:{f}')

#年齡判斷程式
a = input('有無開過車:')
b = input('年齡:')
b = int(b)
if b >= 18:
	if a == '有':
		print('通過測驗了!')
	else:
		print('可以去考駕照喔')
elif b < 18:	
	if a == '有':
		print('你怎麼會開過車!!!')
	else:
		print('再過幾年就可以去考駕照囉')
#最後可以不用加else:

#　while迴圈	      
x = 0 
while x < 10:
	print('x小於10'+'\n'+'我還在執行')
	x = x + 1
	print(f'現在x = {x}')
print('我跑出來了!!!')


#　while True
while True:
	mode = input('請輸入遊戲模式')
	if mode == 'q':
		break #跑出while迴圈
	elif mode == '1':
		print('啟動模式1')
	elif mode == '2':
		print('啟動模式2')
	else:
		print('只能輸入1、２喔')


#密碼重試程式_法1
password = 'a123456'
times = 3 #剩餘機會(最多輸入三次)

while True:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功')
		break
	else:
		times = times - 1
		print(f'密碼錯誤!還有{times}次機會')	
		if times == 0:
			break #注意block，要打在else區塊內

#密碼重試程式_法2
password = 'a123456'
times = 3

while times > 0 :
	times = times - 1
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功')
		break 
	else:	
		print(f'密碼錯誤!還有{times}次機會')	
