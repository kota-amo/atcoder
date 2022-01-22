N, K = map(int, input().split())
a = [list(map(int, input().split())) for i in range(N)]

total =[]*N
for i in range(N-1):
    total[i]= a[i][0]+a[i][1]+a[i][2]
    print(total[i])
