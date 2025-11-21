T = int(input())

def check(num):
    digits = list(map(int,str(num)))
    last=0
    for i in digits:
        if last > i:
            return False
        else:
            last = i
    return True


for case in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))
    max_num = -1
    for i in range(N):
        for j in range(i+1,N):
            if check(A[i]*A[j]):
                max_num = max(max_num,A[i]*A[j])

    print(f"#{case} {max_num}")
