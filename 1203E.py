import math
N =int(input())
sum = 0
k=int(math.sqrt(N))

#Nの平方根で折り返してカウント
#Nの平方根までの時は
for i in range(1,k):
    sum+=((N//i)-(N//(i+1)))*i

for i in range(1,N//k+1):
    sum+=(N//i)

print(sum)
