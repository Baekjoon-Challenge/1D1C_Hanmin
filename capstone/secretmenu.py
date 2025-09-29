import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
recipe = list(map(int, input().split()))
user_input = list(map(int, input().split()))

if N < M:
    print("normal")
else:
    flag = False
    for i in range(N - M +1):
        if user_input[i:i+M] == recipe:
            flag = True
            break
    if flag == True:
        print("secret")
    else:
        print("normal")