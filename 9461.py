import sys
p_n = [1,1,1,2,2,3,4,5,7,9]

for i in range(10,100):
    p_n.append(p_n[i-1]+p_n[i-5])
    
T = int(sys.stdin.readline())
nums = []
for i in range(T):
    nums.append(int(sys.stdin.readline()))
    
for i in nums:
    print(p_n[i-1])