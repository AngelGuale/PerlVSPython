import timeit
from time import time
def funcioncita():
	a=1
	for i in range(0, 100):
		 a=a*20 
	print a


s="""\
a=1
for i in range(0, 100):
	 a=a*20 
print a
"""

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("funcioncita()", setup="from __main__ import funcioncita", number=1))



#inicio=time()
#funcioncita()
#fin=time()-inicio
#print fin
