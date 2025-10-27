import sys
input = sys.stdin.readline

while 1:
    line = input().rstrip()
    if line == ".": break
    stack = []
    balanced = True
    for char in line:
        if char=="(" or char=="[":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                balanced = False
                break
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                balanced = False
                break
    if stack: balanced =False
    if balanced:
        print("yes")
    else:
        print("no")




    

    