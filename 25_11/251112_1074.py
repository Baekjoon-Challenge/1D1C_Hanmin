import sys

input = sys.stdin.readline

N, r, c = map(int,input().split())

length = 2**N
cnt = 0
def search(N, r, c):
    global cnt
    half = (2**N) //2
    if N == 0:
        return
    if r < half and c < half:
        search(N-1,r,c)
    elif r < half and c >= half:
        cnt += 2**(2*N)//4
        search(N-1,r,c-half)
    elif r >= half and c < half:
        cnt += 2**(2*N)//2
        search(N-1,r-half,c)
    else:
        cnt += (2**(2*N)//2 + 2**(2*N)//4)
        search(N-1,r-half,c-half)

search(N,r,c)
print(cnt)

    
