import sys
input = sys.stdin.readline

N = int(input())
paper = []
for i in range(N):
    paper.append(list(map(int,input().split())))

paper_list = [paper]

cnt_blue=0
cnt_white=0

def check_paper(paper_list,N):
    global cnt_blue
    global cnt_white
    for paper in paper_list:
        cnt = 0
        for i in paper:
            cnt += sum(i)
        if cnt==0:
            cnt_white += 1
        elif cnt==N*N:
            cnt_blue += 1
        else:
            top_list = paper[:N//2]
            bot_list = paper[N//2:]
            top_left = []
            top_right = []
            bot_left = []
            bot_right = []
            for i in range(N//2):
                top_left.append(top_list[i][:N//2])
                top_right.append(top_list[i][N//2:])
                bot_left.append(bot_list[i][:N//2])
                bot_right.append(bot_list[i][N//2:])
            new_list = [top_left,top_right, bot_left, bot_right]
            check_paper(new_list,N//2)

check_paper(paper_list, N)
print(cnt_white)
print(cnt_blue)

