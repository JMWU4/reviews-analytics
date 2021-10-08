data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))

print('檔案讀取完了,總共有', len(data), '筆資料')
print(data[0])

sum_len = 0
for d in data:
	sum_len += len(d)

print('留言的平均長度是: ', sum_len/ len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共又', len(new), '筆留言長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(d), '筆留言提到good')
print(good[0])

good = [d for d in data if 'good' in d] # 快寫法
print(good)

bad = ['bad' in d for d in data] # 下面的快寫法
print(bad)

#bad = []
#for d in data:
#	bad.append('bad' in d)
#print(bad)


# 文字計數
wc = {} # word_count
for d in data:
	words = d.split() # 預設空白鑑切割
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Jimmy'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':	
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔!')

print('感謝使用此查詢功能')

























