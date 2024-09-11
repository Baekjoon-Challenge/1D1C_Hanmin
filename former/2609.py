import sys

def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
def lcm(a,b):
    return a*b//gcd(a,b)

nums = list(map(int,sys.stdin.readline().split()))
if nums[0] > nums[1]:
    a = nums[0]
    b = nums[1]
else:
    a = nums[1]
    b = nums[0]
    
print(gcd(a,b))
print(lcm(a,b))