data = []
correspond = []
search = input('請搜尋關鍵字：')
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        if search in line:
            print(line)
            correspond.append(line)
print ('總共有', len(correspond), '筆留言符合')

sum_len = 0
for comment in correspond:
    sum_len += len(comment)
print('平均留言長度為', sum_len / len(correspond), '個字')

see = input('請問你想印出第幾筆資料？')
print(correspond[int(see)])
