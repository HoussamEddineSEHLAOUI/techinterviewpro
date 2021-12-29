# Python program

def gstScor(A):
	num='0123456789'
	alpha='azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN'
	s=0
	for i in A:
		if i in num :
			s+=int(i)
		elif i in alpha :
			s+=1
		elif i ==' ':
			s+=0
		else :
			s+=5
	return s

print(gstScor("a b?c2"))
