import re
import timeit

if __name__ == "__main__":
	import timeit
	data="";
	with open ("Texto1MB.txt",  "r") as myfile:
		import timeit
		data=myfile.read().replace('\n', ' ')
			

	lines = [line.rstrip('\n') for line in open("patronesFile.txt")];
	print "tiempo, long, tipoB, OS,lng,tamTexto";
	for patronstr in lines:
		patron=re.compile(patronstr);
		print  timeit.timeit("re.findall(patron, data)", setup="import re; from __main__ import  patron, data", number=1),",",len(patronstr),",",2,",",7,",",5,",",1;
