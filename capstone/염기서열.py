import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sequences = [input().rstrip() for _ in range(N)]

def can_cover(s1, s2):
    for i in range(M):
        if s1[i] != '.' and s2[i] != '.' and s1[i] != s2[i]:
            return False
    return True

compared = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        compared[i][j] = can_cover(sequences[i], sequences[j])

coverable = [False] * (1 << N)
coverable[0] = True  

for mask in range(1 << N):
    indices = [i for i in range(N) if mask & (1 << i)]
    ok = True
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            if not compared[indices[i]][indices[j]]:
                ok = False
                break
        if not ok:
            break
    coverable[mask] = ok

dp = [N for _ in range(1 << N)]
dp[0] = 0

for mask in range(1 << N):
    remain = mask ^ ((1 << N) - 1) 
    sub = remain
    while sub:
        if coverable[sub]:
            next_mask = mask | sub 
            dp[next_mask] = min(dp[next_mask], dp[mask] + 1)
        
        sub = (sub - 1) & remain


print(dp[-1])