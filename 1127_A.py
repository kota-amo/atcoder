S1 = input()
S2 = input()

l1 = len(S1)
l2 = len(S2)

count = 0
for i in range(2):
	if S1[i]=="#":
		count+=1

for i in range(2):
	if S2[i]=="#":
		count+=1

if count ==4:
	print("Yes")
elif count == 3:
	print("Yes")
elif count == 2:
	if S1[0]=="#" and S2[1]=="#":
		print("No")
	elif S1[1]=="#" and S2[0]=="#":
		print("No")
	else:
		print("Yes")	
