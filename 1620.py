import sys

mn = list(map(int, sys.stdin.readline().split()))
pokemon_list = dict()

for i in range(1,mn[0]+1):
    pokemon_list[i] = sys.stdin.readline().strip()

inverted_list = {v:k for k,v in pokemon_list.items()}
question = []
for i in range(mn[1]):
    question.append(sys.stdin.readline().strip())
    
    
for i in question:
    if i.isdigit():
        print(pokemon_list[int(i)])
    else:
        print(inverted_list[i])