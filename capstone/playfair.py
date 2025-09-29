import sys


message = input()
keys = list(set(input()))

for i in range(int(ord('A')), int(ord('Z')+1)):  
    char = chr(i)
    if char not in keys and char != 'J':
        keys.append(char)

key_map = [['' for _ in range(5)] for _ in range(5)]

n = 0
for i in range(5):
    for j in range(5):
        key_map[i][j] = keys[n]
        n += 1
        

pairs = []

i = 0
while i < len(message):
    if i == len(message) - 1:
        if message[i] == 'X':
            pairs.append(message[i] + 'X')
        else:
            pairs.append(message[i] + 'X')
        break

    if message[i] == message[i + 1]:
        if message[i] == 'X':
            pairs.append(message[i] + 'Q')
        else:
            pairs.append(message[i] + 'X')
        i += 1
    else:
        pairs.append(message[i:i+2])
        i += 2

def find_position(mat, char):
    for i, row in enumerate(mat):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None
    
def encrypt_pair(mat, pair):
    pos1 = find_position(mat, pair[0])
    pos2 = find_position(mat, pair[1])

    if pos1[0] == pos2[0]:
        return mat[pos1[0]][(pos1[1]+1)%5] + mat[pos2[0]][(pos2[1]+1)%5]

    elif pos1[1] == pos2[1]:
        return mat[(pos1[0]+1)%5][pos1[1]] + mat[(pos2[0]+1)%5][pos2[1]]

    else:
        return mat[pos1[0]][pos2[1]] + mat[pos2[0]][pos1[1]]

encrypted = ''.join([encrypt_pair(key_map, pair) for pair in pairs])


print(encrypted)