function asUint8Array(input) {
  if (input instanceof Uint8Array) {
    return input;
  } else if (typeof(input) === 'string') {
    // This naive transform only supports ASCII patterns. UTF-8 support
    // not necessary for the intended use case here.
    var arr = new Uint8Array(input.length);
    for (var i = 0; i < input.length; i++) {
      var c = input.charCodeAt(i);
      if (c > 127) {
        throw new TypeError("Only ASCII patterns are supported");
      }
      arr[i] = c;
    }
    return arr;
  } else {
    // Assume that it's already something that can be coerced.
    return new Uint8Array(input);
  }
}
function boyerMoore(patternBuffer) {
  // Implementation of Boyer-Moore substring search ported from page 772 of
  // Algorithms Fourth Edition (Sedgewick, Wayne)
  // http://algs4.cs.princeton.edu/53substring/BoyerMoore.java.html
  /*
  USAGE:
     // needle should be ASCII string, ArrayBuffer, or Uint8Array
     // haystack should be an ArrayBuffer or Uint8Array
     var search = boyerMoore(needle);
     var skip = search.byteLength;
     var indexes = [];
     for (var i = search(haystack); i !== -1; i = search(haystack, i + skip)) {
       indexes.push(i);
     }
  */
  var pattern = asUint8Array(patternBuffer);
  var M = pattern.length;
  if (M === 0) {
    throw new TypeError("patternBuffer must be at least 1 byte long");
  }
  // radix
  var R = 256;
  var rightmost_positions = new Int32Array(R);
  // position of the rightmost occurrence of the byte c in the pattern
  for (var c = 0; c < R; c++) {
    // -1 for bytes not in pattern
    rightmost_positions[c] = -1;
  }
  for (var j = 0; j < M; j++) {
    // rightmost position for bytes in pattern
    rightmost_positions[pattern[j]] = j;
  }
  function boyerMooreSearch(txtBuffer, start, end) {
    // Return offset of first match, -1 if no match.
    var txt = asUint8Array(txtBuffer);
    if (start === undefined) start = 0;
    if (end === undefined) end = txt.length;
    var pat = pattern;
    var right = rightmost_positions;
    var lastIndex = end - pat.length;
    var lastPatIndex = pat.length - 1;
    var skip;
    for (var i = start; i <= lastIndex; i += skip) {
      skip = 0;
      for (var j = lastPatIndex; j >= 0; j--) {
        var c = txt[i + j];
        if (pat[j] !== c) {
          skip = Math.max(1, j - right[c]);
          break;
        }
      }
      if (skip === 0) {
        return i;
      }
    }
    return -1;
  };
  boyerMooreSearch.byteLength = pattern.byteLength;
  return boyerMooreSearch;
}



function inicializar2(){
	var b=document.getElementById("btnBM");
	b.addEventListener("click", prueba2, false);
	}

function prueba2(){
console.time('Test performance');
var indice = indexOf('conjetura','En teoría de números, la conjetura de Goldbach es uno de los problemas abiertos más antiguos en matemáticas. A veces se le califica del problema más difícil en la historia de esta ciencia. Concretamente, G.H. Hardy en 1921 en su famoso discurso pronunciado en la Sociedad Matemática de Copenhage1 comentó que probablemente la conjetura de Goldbach no es sólo uno de los problemas no resueltos más difíciles de la teoría de números, sino de todas las matemáticas. Su enunciado es el siguiente:'
'Esta conjetura ha sido investigada por muchos teóricos de números y ha sido comprobada por ordenadores para todos los números pares menores que 1018. La mayor parte de los matemáticos creen que la conjetura es cierta, y se basan mayoritariamente en las consideraciones estadísticas sobre la distribución probabilística de los números primos en el conjunto de los números naturales: cuanto mayor sea el número entero par, se hace más «probable» que pueda ser escrito como suma de dos números primos.'
'Sabemos que todo número par puede escribirse de forma mínima como suma de a lo más seis números primos. Como consecuencia de un trabajo de Vinográdov, todo número par lo bastante grande puede escribirse como suma de a lo más cuatro números primos. Además, Vinográdov demostró que casi todos los números pares pueden escribirse como suma de dos números primos (en el sentido de que la proporción de números pares que pueden escribirse de dicha forma tiende a 1). En 1966, Chen Jing-run mostró que todo número par lo bastante grande puede escribirse como suma de un primo y un número que tiene a lo más dos factores primos.'
'Con el fin de generar publicidad para el libro El tío Petros y la conjetura de Goldbach de Apostolos Doxiadis, el editor británico Tony Faber ofreció en 2000 un premio de un millón de dólares a aquel angloparlante que demostrase la conjetura antes de abril de 2002. Nadie reclamó el premio.'
'Goldbach formuló dos conjeturas relacionadas entre sí sobre la suma de números primos:2 la conjetura fuerte de Goldbach y la conjetura débil de Goldbach. La que se discute aquí es la fuerte, y es la que se suele mencionar como «conjetura de Goldbach» a secas.'
'Se ha trabajado mucho en la conjetura débil, culminando en 2013 en una reivindicación del matemático peruano Harald Helfgott3 4 sobre su demostración completa.');
console.timeEnd('Test performance');
console.log(indice);
	}
	

window.addEventListener("load", inicializar2, false);

