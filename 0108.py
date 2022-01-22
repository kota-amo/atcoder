K = int(input())

#文字列で二進数にする
K2 = (format(K , 'b'))

Ans = [0]*(len(K2))
for i in range(len(K2)):
    if K2[i]=="1":
        Ans[i]=2
    elif K2[i]=="0":
        Ans[i]==0

for i in Ans:
    print(i,end="")
