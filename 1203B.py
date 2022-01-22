S = input()
T = "oxx"*(10**5)
print(T)

N = len(S)
M = len(T)
flag = False 
for i in range(M-N+1): 
    if T[i:i+M] == S:  
        flag = True 

# 答えを出力する
if flag: print("Yes")
else: print("No") 



