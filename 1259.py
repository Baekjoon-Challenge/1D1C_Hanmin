import sys

answer = []
while 1:
    num = sys.stdin.readline()
    num = num.replace("\n", "")
    if num == "0":
        break
    
    flag = 0
    for i in range(len(num)//2):
        if num[i] != num[-1-i]:
            flag = 1
    answer.append(flag)
    
        
for i in answer:
    if i:
        print("no") 
    else:
        print("yes")     
    