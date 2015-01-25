#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
from numpy import *

diccionario=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u"
, "v", "w", "x", "y", "z", " "];

texto="";
total=1000000;
for m in range(total):
	import random
	indice=int(random.randrange(27));
	texto=texto+diccionario[indice];

print texto
