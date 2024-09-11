import sys

n = int(sys.stdin.readline())
num = [i for i in range(1,n+1)]
seq = []
stack = []
for i in range(n):
    seq.append(int(sys.stdin.readline()))
    
operation = []
flag = 0    
for i in seq:
    if not stack:
        while 1:
            p = num.pop(0)
            stack.append(p)
            operation.append("+")
            if p == i:
                break
            
        stack.pop()
        operation.append("-")
        
    elif i != stack[-1]:
        if i not in num:
            flag = 1
            break
        while 1:
            p = num.pop(0)
            stack.append(p)
            operation.append("+")
            if p == i:
                break
            
        stack.pop()
        operation.append("-")
    else:
        p = stack.pop()
               
        if p != i:
            flag = 1
            break
        operation.append("-") 
        
if flag == 1:
    print("NO")
else:
    for i in operation:
        print(i)