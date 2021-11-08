n=int(input('enter n value'))
s=0
m=n
while(n!=0):
	r=n%10
	n//=10
	s=s*10+r
if(s==m):
	print('it is palindrome')
else:
	print('it is not palondrome')
