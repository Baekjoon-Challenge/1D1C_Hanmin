from collections import defaultdict
T = int(input())

def dfs(cur,visited,remain):
    global ans

    if remain == 0:
        ans = max(ans,int(cur))
        return
    
    if cur in visited[remain]:
        return



for i in range(1,T+1):
    num, change = map(int,input().split())
    num = list(map(int, str(num)))
    max_num = max(num)
    length  = len(num)
    ans = 0
    visited = [set()]
    

