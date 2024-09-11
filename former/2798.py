a, b = map(int,input().split())
cards = list(map(int,input().split()))

max_sum = 0

for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            sum = cards[i] + cards[j] + cards[k]
            if sum > b:
                continue
            if sum > max_sum:
                max_sum = sum

print(max_sum)