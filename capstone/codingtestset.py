def test(num):
    ptable = [0] * N
    ptable[0] = clist[0]
    for i in range(N-1):
        if ptable[i] >= num:
            ptable[i+1] = clist[i+1] + dlist[i]
        elif ptable[i] + dlist[i] >= num:
            ptable[i+1] = clist[i+1] + (ptable[i] + dlist[i] - num)
        else:
            return False
    if ptable[N-1] >= num:
        return True
    else:
        return False

def BinSearch(start, end):
    if start > end:
        return BinSearch(start-1, end)
    mid = (start + end) // 2
    if test(mid):
        if start == end:
            return start
        else:
            return BinSearch(mid+1, end)
    else:
        return BinSearch(start, mid-1)

N, T = map(int, input().split())

for i in range(T):
    clist = []
    dlist = []
    problems = list(map(int, input().split()))
    for j in range(len(problems)):
        if (j % 2):
            dlist.append(problems[j])
        else:
            clist.append(problems[j])
    print(BinSearch(0, 2*(10**12)))