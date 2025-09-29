import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
scores = []
total = [0] * n

for _ in range(3):
    cur = list(map(int, input().split()))
    scores.append(cur)
    for i in range(n):
        total[i] += cur[i]
scores.append(total)

for score in scores:
    score_counter = Counter(score)
    score_set = list(set(score))
    score_set.sort(reverse=True)
    score_dic = dict()
    
    token = 1
    for s in score_set:
        score_dic[s] = token
        token += score_counter[s]
        
    result = []
    for i in score:
        result.append(score_dic[i])
    print(*result)
