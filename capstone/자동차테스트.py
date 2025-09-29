import sys

input = sys.stdin.readline
n, q = map(int, input().split())
car = sorted(map(int,input().split()))

car_dic = {}
for i in range(n):
    car_dic[car[i]] = (i)*(n-1-i)

for j in range(q):
    m = int(input())
    
    if car_dic.get(m):
        print(car_dic[m])
    else:
        print(0)