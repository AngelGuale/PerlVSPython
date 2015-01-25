# !/usr/bin/perl


  use Benchmark qw(:all) ;
   use Benchmark qw( :hireswallclock ) ;
  use Time::HiRes qw(time);
    use File::Slurp qw( :all ) ;
	use Tie::File;


$Sigma = 256; # The size of the alphabet.
sub boyer_moore_bad_character {
my ( $P ) = @_; # The pattern.
use integer;
my ( $m, $i, $j ) = ( length( $P ) );
my @bc = ( $m ) x $Sigma;
for ( $i = 0, $j = $m - 1; $i < $m; $i++ ) {
$bc[ ord( substr( $P, $i, 1 ) ) ] = $j--;
}
return ( $m, @bc ); # Length of pattern and bad-character rule.
}



sub boyer_moore_good_suffix {
my ( $P, $m ) = @_; # The pattern and its length.
use integer;
my ($i, $j, $k, @k);
my ( @gs ) = ( 0 ) x ( $m + 1 );
$k[ $m ] = $j = $m + 1;
for ( $i = $m; $i > 0; $i-- ) {
while ( $j <= $m &&substr( $P, $i - 1, 1 ) ne substr($P, $j - 1, 1)) {
$gs[ $j ] = $j - $i if $gs[ $j ] == 0;
$j = $k[ $j ];
}
$k[ $i - 1 ] = --$j;
}
$k = $k[ 0 ];
for ($j = 0; $j <= $m; $j++ ) {
$gs[ $j ] = $k
if $gs[ $j ] == 0;
$k
= $k[ $k ] if
$j
== $k;
}
shift @gs;
return @gs; # Good suffix rule.
}




sub boyer_moore {
	
 my ( $T, $P ) = @_; # The text and the pattern.
 use integer;
 my ( $m, @bc ) = boyer_moore_bad_character( $P );
 my ( @gs ) = boyer_moore_good_suffix( $P, $m );
 my ( $i, $last_i, $first_j, $j ) = ( 0, length( $T ) - $m, $m - 1 );
 while ( $i <= $last_i ) {
 for ( $j = $first_j;
 $j >= 0 &&
 substr( $T, $i + $j, 1) eq substr( $P, $j, 1 );
 --$j )
 {
 # Decrement $j until a mismatch is found.
 }
 if ( $j < 0 ) {
	
 return $i; # Match.
 # If we were returning all the matches instead of just
 # the first one, we would do something like this:
 # push @i, $i;
 # $i + $gs[ $j + 1 ];
 # and in the end of the function:
 # return @i;
 } else {
 my $bc = $bc[ ord( substr($T, $i + $j, 1) ) ] - $m + $j + 1;
 my $gs = $gs[ $j ];
 $i += $bc > $gs ? $bc : $gs; # Choose the larger skip.
 }
 }
  return -1; # Mismatch.
}

$file="result/textoPrueba1.txt";
$texto = read_file($file);

tie @patrones, 'Tie::File', "patronesFile.txt" or die;


print "tiempo, long_patt\n";
foreach $patron(@patrones) {
	$x=timeit(1,'&boyer_moore($texto, $patron);');
	print $x->real, ",", length($patron);
	print "\n";
}
#print "\ntamanio: ", length($texto), " patron: ", $patron, "\n";
