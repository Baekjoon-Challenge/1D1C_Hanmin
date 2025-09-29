import sys

n,k = map(int,input().split())
tree = {}
indegree = [0 for _ in range(n+1)]
for i in range(1,n+1):
    x = list(map(int,input().split()))
    if x[0]:
        tree[i]=x[1:]
        for x_ in x[1:]:
            indegree[x_]+=1

answer = [0 for _ in range(n+1)]
answer[1]=k
stk = [[1,k]]
while stk:
    node,req = stk.pop()
    if node in tree.keys():
        cyc, remain = req//len(tree[node]), req%len(tree[node])
        for i, nxt in enumerate(tree[node]):
            if indegree[nxt]: # 간선이 남아있는 경우 덧셈만 해준다
                indegree[nxt]-=1
                if i<remain:
                    answer[nxt]+=cyc+1
                else:
                    answer[nxt]+=cyc
            if not indegree[nxt]: # 간선이 없는 경우 다음 자식 노드에 트래픽을 분산할 준비를 한다
                stk.append((nxt,answer[nxt]))
    
print(*answer[1:],sep=' ')
