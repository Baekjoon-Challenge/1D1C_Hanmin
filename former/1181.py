import sys

n = int(sys.stdin.readline())
words = []
for i in range(n):
    words.append(sys.stdin.readline())

words = list(set(words))
words.sort(key=len)

start = 0
end = 0

prev = words[0] 
length = len(words)
for i in range(length):
    if len(words[i]) != len(prev):
        end = i
        temp = words[start:end]
        temp.sort()
        words[start:end] = temp[:]
        start = end
        
    elif i == length-1:
        temp = words[start:]
        temp.sort()
        words[start:] = temp[:]
    prev = words[i]
    
for i in words:
    print(i,end = "")
print()
