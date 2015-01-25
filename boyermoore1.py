# -*- encoding: utf-8 -*-
# Boyer Moore String Search implementation in Python
# Ameer Ayoub <ameer.ayoub@gmail.com>
from timeit import timeit
from time import time
# Generate the Bad Character Skip List
def generateBadCharShift(term):
    skipList = {}
    for i in range(0, len(term)-1):
        skipList[term[i]] = len(term)-i-1
    return skipList

# Generate the Good Suffix Skip List
def findSuffixPosition(badchar, suffix, full_term):
    for offset in range(1, len(full_term)+1)[::-1]:
        flag = True
        for suffix_index in range(0, len(suffix)):
            term_index = offset-len(suffix)-1+suffix_index
            if term_index < 0 or suffix[suffix_index] == full_term[term_index]:
                pass
            else:
                flag = False
        term_index = offset-len(suffix)-1
        if flag and (term_index <= 0 or full_term[term_index-1] != badchar):
            return len(full_term)-offset+1

def generateSuffixShift(key):
    skipList = {}
    buffer = ""
    for i in range(0, len(key)):
        skipList[len(buffer)] = findSuffixPosition(key[len(key)-1-i], buffer, key)
        buffer = key[len(key)-1-i] + buffer
    return skipList
    
# Actual Search Algorithm
def BMSearch(haystack, needle):
    goodSuffix = generateSuffixShift(needle)
    badChar = generateBadCharShift(needle)
    i = 0
    while i < len(haystack)-len(needle)+1:
        j = len(needle)
        while j > 0 and needle[j-1] == haystack[i+j-1]:
            j -= 1
        if j > 0:
            badCharShift = badChar.get(haystack[i+j-1], len(needle))
            goodSuffixShift = goodSuffix[len(needle)-j]
            if badCharShift > goodSuffixShift:
                i += badCharShift
            else:
                i += goodSuffixShift
        else:
            return i
    return -1

if __name__ == "__main__":
	import timeit
	block = "This is a simple example"
	texto="""En teoria de números, la conjetura de Goldbach es uno de los problemas abiertos mas antiguos en matematicas. A veces se le califica del problema más difícil en la historia de esta ciencia. Concretamente, G.H. Hardy en 1921 en su famoso discurso pronunciado en la Sociedad Matemática de Copenhage1 comentó que probablemente la conjetura de Goldbach no es sólo uno de los problemas no resueltos más difíciles de la teoría de números, sino de todas las matemáticas. Su enunciado es el siguiente:'+
	'Esta conjetura ha sido investigada por muchos teóricos de números y ha sido comprobada por ordenadores para todos los números pares menores que 1018. La mayor parte de los matemáticos creen que la conjetura es cierta, y se basan mayoritariamente en las consideraciones estadísticas sobre la distribución probabilística de los números primos en el conjunto de los números naturales: cuanto mayor sea el número entero par, se hace más «probable» que pueda ser escrito como suma de dos números primos.'+
	'Sabemos que todo número par puede escribirse de forma mínima como suma de a lo más seis números primos. Como consecuencia de un trabajo de Vinográdov, todo número par lo bastante grande puede escribirse como suma de a lo más cuatro números primos. Además, Vinográdov demostró que casi todos los números pares pueden escribirse como suma de dos números primos (en el sentido de que la proporción de números pares que pueden escribirse de dicha forma tiende a 1). En 1966, Chen Jing-run mostró que todo número par lo bastante grande puede escribirse como suma de un primo y un número que tiene a lo más dos factores primos.'+
	'Con el fin de generar publicidad para el libro El tio Petros y la conjetura de Goldbach de Apostolos Doxiadis, el editor británico Tony Faber ofreció en 2000 un premio de un millón de dólares a aquel angloparlante que demostrase la conjetura antes de abril de 2002. Nadie reclamó el premio.'+
	'Goldbach formulo dos conjeturas relacionadas entre sí sobre la suma de números primos:2 la conjetura fuerte de Goldbach y la conjetura débil de Goldbach. La que se discute aquí es la fuerte, y es la que se suele mencionar como «conjetura de Goldbach» a secas.'+
	'Se ha trabajado mucho en la conjetura débil, culminando en 2013 en una reivindicación del matemático peruano Harald Helfgott3 4 sobre su demostración completa."""
	#patron="un padre";
	#patrones=["amor", "odio", "un padre", "agua","aire","desgracia","edad","ciudad","pais","los prejuicios","enormes enigmas",
	#"nombre","tecnologia","futuro","pasado", "hermosos dias", "nn", "flores", "mensaje", "as","alto", "bajo", "noche",
	#"una sola cosa", "joven", "anciano", "uno", "dos", "pez", "no cumple con su tarea"];
	patrones = [line.rstrip('\n') for line in open("patronesFile.txt")];

	data="";
	with open ("result/textoPrueba1.txt", "r") as myfile:
		import timeit
		data=myfile.read().replace('\n', ' ')
		
	
	print "tiempo, long_patt";
	for patron in patrones:
		print  timeit.timeit("BMSearch(data, patron)", setup="from __main__ import BMSearch, texto, patron, data", number=1),",",len(patron);
		#print "\n"
	
	#print "longitud: ", len(data)
