data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
print ('總共有', len(data), '筆留言')

sum_len = 0
for comment in data:
    sum_len += len(comment)
print('平均留言長度為', sum_len / len(data), '個字')