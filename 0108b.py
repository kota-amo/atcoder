import math

N = int(input())
a = [0] * N   #長さNの配列を作る。値は0で初期化。
b = [0] * N
for i in range(N):
   a[i], b[i] = map(int, input().split()) #aとbの配列として保持される。
# for文を出たら配列a,bに対して何か操作を行って出力を行う。

len = []
for i in range(0, N-1):
    for j in range(i+1, N):
        len.append( math.sqrt((a[j]-a[i])**2 + (b[j]-b[i])**2) )
        
len.sort(reverse=True)
print(len[0])



