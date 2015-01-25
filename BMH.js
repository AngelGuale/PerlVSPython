function boyer_moore_horspool(haystack, needle) {
    var badMatchTable = {};
    var maxOffset = haystack.length - needle.length;
    var offset = 0;
    var last = needle.length - 1;
    var scan;
  
    // Generate the bad match table, which is the location of offsets
    // to jump forward when a comparison fails
    Array.prototype.forEach.call(needle, function (char, i) {
        badMatchTable[char] = last - i;
    });
 
    // Now look for the needle
    while (offset <= maxOffset) {
        // Search right-to-left, checking to see if the current offset at 
        // needle and haystack match.  If they do, rewind 1, repeat, and if we 
        // eventually match the first character, return the offset.
        for (scan=last; needle[scan] === haystack[scan+offset]; scan--) {
            if (scan === 0) {
              return offset;
            }
        }
 
        offset += badMatchTable[haystack[offset + last]] || last;
    }
 
    return -1;
}
 
var stringLocation = boyer_moore_horspool('because sometimes algorithms are more fun than str.search()', 'algorithms');
 
console.log(stringLocation);
function inicializar(){
	var b=document.getElementById("btn");
	b.addEventListener("click", prueba, false);
	}

function prueba(){
console.profile("TP");
	var a=performance.now();
var stringLocation = boyer_moore_horspool('because sometimes algorithms are more fun than str.search()', 'algorithms');
console.profileEnd();
var b=performance.now();
console.log("tiempo: "+(b-a));
console.log(stringLocation);
	}
	

window.addEventListener("load", inicializar, false);
