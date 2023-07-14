# data = []
import collections
from collections import Counter
'''
#응답 코드가 '200'인 것의 개수
cnt = 0
with open('./data/log.txt', 'r') as log:
    for line in log :
        ar = line.split(" ")
        if ar[8] == '200':
            cnt += 1
print(cnt)

#ip별 접속 횟수 개수
ipcnt = {}
with open('./data/log.txt', 'r') as log:
    for line in log :
        ar = line.split()
        # ipcnt.get 을 이용해서 key 없으면 0으로 초기화
        ipcnt[ar[0]] = ipcnt.get(ar[0], 0)+1

for i in ipcnt :
    print(i, " : ", ipcnt[i])

#ip별 트래픽 합계 - dict 이용
traffic = {}

with open('./data/log.txt', 'r') as log:
    for line in log :
        ar = line.split()
        if ar[9].isdigit():
            traffic[ar[0]] = traffic.get(ar[0], 0) + int(ar[9])

for i in traffic :
    print(i, " : ", traffic[i])

'''
# ip별 트래픽 합계 - counter 이용
counter = Counter()
with open('./data/log.txt', 'r') as log:
    for line1 in log :
        ar = line1.split()
        if ar[9].isdigit():
            counter[ar[0]] += int(ar[9])
for i in counter:
    print(i, " : ", counter[i])

