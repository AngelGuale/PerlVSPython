#!/usr/bin/perl


  use Benchmark qw(:all) ;
  use Benchmark qw( :hireswallclock ) ;
  use Time::HiRes qw(time);
  use File::Slurp qw( :all ) ;
  use Tie::File;


$file="textoPrueba1.txt";
$texto = read_file($file);

tie @patrones, 'Tie::File', "patronesFile.txt",recsep=>"\n" or die;

sub buscaTodas{
	$t=shift(@_);
	$patron=shift(@_);
	while($t=~m/$patron/g){
		#do something
		}
	
	
}

print "tiempo, long_patt, OS\n";
foreach $patron(@patrones) {
	$x=timeit(1,'&buscaTodas($texto, $patron);');
	print $x->real, ",", length($patron),",",0;
	print "\n";
}
