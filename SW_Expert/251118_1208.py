for i in range(1,11):
    dump = int(input())
    heights = list(map(int,input().split()))

    for j in range(dump):
        heights.sort()
        heights[0] += 1
        heights[-1] -= 1
    heights.sort()
    print("#%d %d" %(i,heights[-1]-heights[0]))