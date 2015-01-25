#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
from numpy import *

diccionario=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u"
, "v", "w", "x", "y", "z", " "];
tamaniomuestra=384;

longitudes=zeros(tamaniomuestra);
#print longitudes;

#patrones=zeros(30);
patrones = array(["12345678901234567890123456789012345678" for _ in range(tamaniomuestra)]);
#print patrones
for i in range(tamaniomuestra):
	import random
	longitud= int(random.randrange(30));
	longitudes[i]=int(longitud)+1;

#print longitudes;

for i in range(tamaniomuestra):
	import random
	longi=int(longitudes[i]);
	patrones[i]="";
	for j in range(longi):
	#	print "jota: ", j;
		indice=random.randrange(27)
		#print patrones[i];
		patrones[i]=patrones[i]+diccionario[indice];
		#print patrones[i];
	
for k in range(len(patrones)):
	print patrones[k]

