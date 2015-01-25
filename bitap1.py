# -*- encoding: utf-8 -*-
# Shift-Or / Bitap / Baeza Yates Gonnet
# https://github.com/polovik/Algorithms/blob/master/bitap.py
from timeit import timeit
from time import time

	
#intento de shift-or


"""Auxiliary procedure for printing each item of row in columns in binary form
"""
import sys
"""def _printTable(t, size):
    out = ""
    for i in range(len(t)):
        binaryForm = bin(t[i])
        binaryForm = binaryForm[2 : ]
        binaryForm = binaryForm.zfill(size)
        out += binaryForm + ", "
    out = out[ : -2]
    print out"""

"""Bitap (Shift-Or) fuzzy searching algorithm with Wu-Manber modifications.
http://habrahabr.ru/post/114997/
http://habrahabr.ru/post/132128/
http://ru.wikipedia.org/wiki/Двоичный_алгоритм_поиска_подстроки
Search needle(pattern) in haystack(real word from text) with maximum alterations = maxErrors.
If maxErrors equal 0 - execute precise searching only.
Return approximately place of needle in haystack and number of alterations.
If needle can't find with maxErrors alterations, return tuple of empty string and -1.
"""
def _generateAlphabet(needle, haystack):
    alphabet = {}
    for letter in haystack:
        if letter not in alphabet:
            letterPositionInNeedle = 0
            for symbol in needle:
                letterPositionInNeedle = letterPositionInNeedle << 1
                letterPositionInNeedle |= int(letter != symbol)
            alphabet[letter] = letterPositionInNeedle
    return alphabet

def bitapSearch(haystack, needle, maxErrors):
    haystackLen = len(haystack)
    needleLen = len(needle)

    """Genarating mask for each letter in haystack.
    This mask shows presence letter in needle.
    """
    

    alphabet = _generateAlphabet(needle, haystack)

    table = [] # first index - over k (errors count, numeration starts from 1), second - over columns (letters of haystack)
    emptyColumn = (2 << (needleLen - 1)) - 1

    #   Generate underground level of table
    underground = []
    [underground.append(emptyColumn) for i in range(haystackLen + 1)]
    table.append(underground)
    #_printTable(table[0], needleLen)

    #   Execute precise matching
    k = 1
    table.append([emptyColumn])
    for columnNum in range(1, haystackLen + 1):
        prevColumn = (table[k][columnNum - 1]) >> 1
        letterPattern = alphabet[haystack[columnNum - 1]]
        curColumn = prevColumn | letterPattern
        table[k].append(curColumn)
        if (curColumn & 0x1) == 0:
            place = haystack[columnNum - needleLen : columnNum]
            return (place, k - 1)
    #_printTable(table[k], needleLen)

    #   Execute fuzzy searching with calculation Levenshtein distance
    for k in range(2, maxErrors + 2):
        print "Errors =", k - 1
        table.append([emptyColumn])

        for columnNum in range(1, haystackLen + 1):
            prevColumn = (table[k][columnNum - 1]) >> 1
            letterPattern = alphabet[haystack[columnNum - 1]]
            curColumn = prevColumn | letterPattern
            
            insertColumn = curColumn & (table[k - 1][columnNum - 1])
            deleteColumn = curColumn & (table[k - 1][columnNum] >> 1)
            replaceColumn = curColumn & (table[k - 1][columnNum - 1] >> 1)
            resColumn = insertColumn & deleteColumn & replaceColumn
            
            table[k].append(resColumn)
            if (resColumn & 0x1) == 0:
                startPos = max(0, columnNum - needleLen - 1) # taking in account Replace operation
                endPos = min(columnNum + 1, haystackLen) # taking in account Replace operation
                place = haystack[startPos : endPos]
                return (place, k - 1)
            
        #_printTable(table[k], needleLen)
    return ("", -1)

"""Highlight letters in fullWord, which concur with letters in pattern with same order.
wordPart - it's a part of fullWord, where matching with pattern letters will execute.
"""
class bitapHighlighter():
    def __init__(self, fullWord, wordPart, pattern):
        self._fullWord = fullWord
        self._wordPart = wordPart
        self._pattern = pattern
        self._largestSequence = ""
    
    """Finding longest sequence of letters in word. Letters must have same order, as in pattern
    """
    def _nextSequence(self, fromPatternPos, fromWordPos, prevSequence):
        for patternPos in range(fromPatternPos, len(self._pattern)):
            char = self._pattern[patternPos]
            for wordPos in range(fromWordPos, len(self._wordPart)):
                if char == self._wordPart[wordPos]:
                    sequence = prevSequence + char
                    self._nextSequence(patternPos + 1, wordPos + 1, sequence)
        if len(self._largestSequence) < len(prevSequence):
            self._largestSequence = prevSequence

    """Divide fullWord on parts: head, place(wordPart) and tail.
    Select each letter of wordPart, which present in _largestSequence with <b></b> tags
    Return gathered parts in one highlighted full word
    """
    def _gatherFullWord(self):
        placePos = self._fullWord.find(self._wordPart)
        head = self._fullWord[0 : placePos]
        tail = self._fullWord[placePos + len(self._wordPart) : ]
        highlightedPlace = ""
        for symbol in self._wordPart:
            if symbol == self._largestSequence[0 : 1]:
                highlightedPlace += "<b>" + symbol + "</b>"
                self._largestSequence = self._largestSequence[1 : ]
            else:
                highlightedPlace += symbol
        return head + highlightedPlace + tail
    
    """Run highlighting and return highlited word.
    """
    def getHighlightedWord(self):
        self._nextSequence(0, 0, "")
        return self._gatherFullWord()

"""haystack = sys.argv[1]
needle = sys.argv[2]
errorsCount = sys.argv[3]
print "haystack = " + haystack + ". needle = " + needle + ". errorsCount = " + errorsCount

#   Display letters of haystack in columns
out = ""
out = out.ljust(len(needle) + 2)
for i in range(len(haystack)):
    out += haystack[i].ljust(len(needle)) + "  "
out = out[ : -2]
print out

#   Start bitap searching
(needlePlace, errors) = bitapSearch(haystack, needle, int(errorsCount))
print "Result of Bitap searching:", needlePlace, errors
print bitapHighlighter(haystack, needlePlace, needle).getHighlightedWord()"""


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
	patrones = [line.rstrip('\n') for line in open("patronesFile.txt")];

	data="";
	with open ("texto140.txt", "r") as myfile:
		import timeit
		data=myfile.read().replace('\n', ' ')
		
	
	print "tiempo, patron";
	for patron in patrones:
		print  timeit.timeit("bitapSearch(data, patron, 0)", setup="from __main__ import bitapSearch, texto, patron, data", number=1),",",patron;
		#print "\n"
	
	#print "longitud: ", len(data)
