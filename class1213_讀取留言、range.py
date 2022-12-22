#cd 位置、dir 顯示資料夾中的檔案

#讀取留言數程式1
data = []
with open('reviews.txt','r') as f: #f可以換成其他變數
	for line in f: #一行一行讀取
		data.append(line)
print('總共有',len(data),'筆資料')

#讀取留言數程式2(顯示運行過程)
data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count +=1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完，總共有',len(data),'筆資料')

#以下三個迴圈都是利用清單data[]的內容
#計算留言平均長度
sum_len = 0 
for d in data:
	sum_len = sum_len + len(d)
		#print(sum_len)
avg = sum_len/len(data)  #全部留言長度/data筆數
print('留言平均長度為:',avg)

#篩選範例1
new = [d for d in data if len(d) < 100] #快寫法
# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
print('共有',len(new),'個符合') #篩選字串長度<100
print(new[0])

#list快寫法(省時): output=[運算 for 變數 in 清單 if 篩選條件]

#篩選有多少留言提到'good'
good = [d for d in data if 'good' in d] #快寫法
# good = []
# for d in data:
# 	if 'good' in d:
		# good.append(d)
print('共有',len(good),'筆留言提到good') #		
print(good[0])
#篩選有多少留言提到'bad'
bad = [d for d in data if 'bad' in d]
print('共有',len(bad),'筆留言提到bad') #		
print(bad[0])


'''range(內建功能):清單產生器
1.range(結尾值)
2.range(開始值,結尾值)
3.range(開始值,結尾值,遞增值)
'''
for i in range(5): #range(結尾值) 長度為5
	print(i) 
print('-------------------') 

for i in range(1,5): #range(結尾值) 長度為5
	print(i) 
print('-------------------') 

for i in range(1,10,2): #range(結尾值) 長度為5
	print(i) 
