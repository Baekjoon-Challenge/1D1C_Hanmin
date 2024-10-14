import sys

str_a = [0] + list(sys.stdin.readline().rstrip())
str_b = [0] + list(sys.stdin.readline().rstrip())

LCS = [[0 for i in range(len(str_a))]for j in range(len(str_b))]

def lcs_length(LCS, str_a, str_b):
    len_a = len(str_a)
    len_b = len(str_b)

    for i in range(len(str_b)):
        for j in range(len(str_a)):
            if i==0 or j==0:
                LCS[i][j]=0
            elif str_b[i] == str_a[j]:
                LCS[i][j] = LCS[i-1][j-1] + 1
                
            else:
                LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
    
    return LCS[len(str_b)-1][len(str_a)-1]


print(lcs_length(LCS, str_a,str_b))


    

