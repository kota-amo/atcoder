A, B = map(int,input().split())
a = str(A)
b = str(B)
la= len(a)
lb= len(b)

m = min(la,lb)

flag = False
for i in range(m):
   if int(a[la-1-i])+int(b[lb-1-i]) >= 10: 
       flag = True
       break
if flag == True:
    print("Hard")
else:
    print("Easy")