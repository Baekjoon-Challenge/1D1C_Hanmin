import sys

T = int(sys.stdin.readline())

targets= []
cases = []

for i in range(T):
    targets.append(list(map(int,sys.stdin.readline().split())))
    cases.append(list(map(int,sys.stdin.readline().split())))

result = []
for i in range(T):
    ind = targets[i][1]
    cnt = 0
    while 1:
        max_ind = cases[T].index(max(cases[T]))
        if max_ind == ind:
            result.append(cnt)
        elif max_ind < ind:
            for j in range(max_ind):
                cases[T].append(cases[T].pop(0))
            cases[T].pop(0)
            cnt += 1
        
                
        