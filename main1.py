n=int(input('enter n value'))
s=0
m=n
for i in range(1,n):
	if(i%n==0):
	s=s+i
if(s==m):
	print('it is perfect')
else:
	print('it is not perfect')