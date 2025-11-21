for case in range(1,11):
    n = int(input())
    password = list(map(int, input().split()))

    flag = True
    while flag:
        for i in range(1,6):
            first = password.pop(0)
            if first-i > 0:
                password.append(first-i)
            else:
                password.append(0)
                flag = False
                break

    print(f"#{case} {' '.join(map(str,password))}" )

            
