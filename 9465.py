T = int(input())
for i in range(T):
    n = int(input())
    line1 = input()
    line2 = input()
    arr = [list(map(int,line1.split())), list(map(int,line2.split()))]
    for j in range(2):
        for k in range(n):
            adj = [[],[]]
            if j == 0:
                if k==0:
                    adj[j].append(arr[j][k+1]+ arr[j+1][k])
                elif k==n-1:
                    adj[j].append(arr[j][k-1]+arr[j+1][k])
                else:
                    adj[j].append(arr[j][k+1]+arr[j][k-1]+arr[j+1][k])
            else:
                if k==0:
                    adj[j].append(arr[j][k+1]+ arr[j-1][k])
                elif k==n-1:
                    adj[j].append(arr[j][k-1]+arr[j-1][k])
                else:
                    adj[j].append(arr[j][k+1]+arr[j][k-1]+arr[j-1][k])
    print(arr)
    print(adj)
            
        
