import sys
input = sys.stdin.readline

light = {'0': '1110111',
         '1': '0010010',
         '2': '1011101',
         '3': '1011011',
         '4': '0111010',
         '5': '1101011',
         '6': '1101111',
         '7': '1110010',
         '8': '1111111',
         '9': '1111011',
         ' ': '0000000'}
T = int(input())
for i in range(T):
    A, B = input().split()
    A = (5-len(A)) * " " + A
    B = (5-len(B)) * " " + B

    change = 0
    for i in range(5):
        for j in range(7):
            if light[A[i]][j] != light[B[i]][j]:
                change += 1
    
    print(change)