
  alphabetSize= 256;
  
function prueba2(){
var texto='En teoría de números, la conjetura de Goldbach es uno de los problemas abiertos más antiguos en matemáticas. A veces se le califica del problema más difícil en la historia de esta ciencia. Concretamente, G.H. Hardy en 1921 en su famoso discurso pronunciado en la Sociedad Matemática de Copenhage1 comentó que probablemente la conjetura de Goldbach no es sólo uno de los problemas no resueltos más difíciles de la teoría de números, sino de todas las matemáticas. Su enunciado es el siguiente:'+
'Esta conjetura ha sido investigada por muchos teóricos de números y ha sido comprobada por ordenadores para todos los números pares menores que 1018. La mayor parte de los matemáticos creen que la conjetura es cierta, y se basan mayoritariamente en las consideraciones estadísticas sobre la distribución probabilística de los números primos en el conjunto de los números naturales: cuanto mayor sea el número entero par, se hace más «probable» que pueda ser escrito como suma de dos números primos.'+
'Sabemos que todo número par puede escribirse de forma mínima como suma de a lo más seis números primos. Como consecuencia de un trabajo de Vinográdov, todo número par lo bastante grande puede escribirse como suma de a lo más cuatro números primos. Además, Vinográdov demostró que casi todos los números pares pueden escribirse como suma de dos números primos (en el sentido de que la proporción de números pares que pueden escribirse de dicha forma tiende a 1). En 1966, Chen Jing-run mostró que todo número par lo bastante grande puede escribirse como suma de un primo y un número que tiene a lo más dos factores primos.'+
'Con el fin de generar publicidad para el libro El tío Petros y la conjetura de Goldbach de Apostolos Doxiadis, el editor británico Tony Faber ofreció en 2000 un premio de un millón de dólares a aquel angloparlante que demostrase la conjetura antes de abril de 2002. Nadie reclamó el premio.'+
'Goldbach formuló dos conjeturas relacionadas entre sí sobre la suma de números primos:2 la conjetura fuerte de Goldbach y la conjetura débil de Goldbach. La que se discute aquí es la fuerte, y es la que se suele mencionar como «conjetura de Goldbach» a secas.'+
'Se ha trabajado mucho en la conjetura débil, culminando en 2013 en una reivindicación del matemático peruano Harald Helfgott3 4 sobre su demostración completa.';
var patron='2013';
for(i=0;i<50; i++){
console.time('Test performance');
indexOf2(patron,texto);
console.timeEnd('Test performance');

}
	}
  
  /*
    Returns the index of the first occurence of
    the `needle` buffer within the `haystack` buffer.
    
    @param {Buffer} needle
    @param {Buffer} haystack
    @return {Integer}
  */
  function indexOf2(needle, haystack) {
    
    var i, k;
    var n = needle.length;
    var m = haystack.length;
    
    if( n === 0 ) return n;
    
    var charTable = this.makeCharTable( needle );
    var offsetTable = this.makeOffsetTable( needle );
    
    for( i = n - 1; i < m; ) {
      for( k = n - 1; needle[k] === haystack[i]; --i, --k ) {
        if( k === 0 ) return i;
      }
      // i += n - k; // for naive method
      i += Math.max( offsetTable[ n - 1 - k ], charTable[ haystack[i] ] );
    }
    
    return -1;
    
  }
  
  /*
    Makes the jump table based on the
    mismatched character information.
    
    @param {Buffer} needle
    @return {Buffer}
  */
   function makeCharTable( needle ) {
    
    var table = new Uint32Array( this.alphabetSize );
    var n = needle.length;
    var t = table.length;
    var i = 0;
    
    for( ; i < t; ++i ) {
      table[i] = n;
    }
    
    n--;
    
    for( i = 0; i < n; ++i ) {
      table[ needle[i] ] = n - i;
    }
    
    return table;
    
  }
  
  /*
    Makes the jump table based on the
    scan offset which mismatch occurs.
    
    @param {Buffer} needle
  */
   function  makeOffsetTable( needle ) {
    
    var i, suffix;
    var n = needle.length;
    var m = n - 1;
    var lastPrefix = n;
    var table = new Uint32Array( n );
    
    for( i = m; i >= 0; --i ) {
      if( this.isPrefix( needle, i + 1 ) ) {
        lastPrefix = i + 1;
      }
      table[ m - i ] = lastPrefix - i + m;
    }
    
    for( i = 0; i < n; ++i ) {
      suffix = this.suffixLength( needle, i );
      table[ suffix ] = m - i + suffix;
    }
    
    return table;
    
  }
  
  /*
    Is `needle[i:end]` a prefix of `needle`?
    
    @param {Buffer} needle
    @param {Integer} i
  */
   function isPrefix( needle, i ) {
    
    var k = 0;
    var n = needle.length;
    
    for( ; i < n; ++i, ++k ) {
      if( needle[i] !== needle[k] ) {
        return false;
      }
    }
    
    return true;
    
  }
  
  /*
    Returns the maximum length of the
    substring ends at `i` and is a suffix.
    
    @param {Buffer} needle
    @param {Integer} i
  */
   function suffixLength( needle, i ) {
    
    var k = 0;
    var n = needle.length;
    var m = n - 1;
    
    for( ; i >= 0 && needle[i] === needle[m]; --i, --m ) {
      k += 1;
    }
    
    return k;
    
  }
  


function inicializar2(){
	var b=document.getElementById("btnBM");
	b.addEventListener("click", prueba2, false);
	}

	

window.addEventListener("load", inicializar2, false);

