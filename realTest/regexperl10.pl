#!/usr/bin/perl


  use Benchmark qw(:all) ;
  use Benchmark qw( :hireswallclock ) ;
  use Time::HiRes qw(time);
  use File::Slurp qw( :all ) ;
  use Tie::File;


$file="Texto10MB.txt";
$texto = read_file($file);

tie @patrones, 'Tie::File', "patronesFile.txt" or die;

sub buscaTodas{
	$t=shift(@_);
	$patron=shift(@_);
	while($t=~m/$patron/g){
		#do something
		}
	
	
}
#lng 4 es perl
#6 es linux
#2 es total
#tamTeto en MB
print "tiempo, long, tipoB, OS , lng,tamTexto \n";
foreach $patron(@patrones) {
	$x=timeit(1,'&buscaTodas($texto, $patron);');
	print ($x->real, ",", length($patron),",",2,",",6,",",4,",",10);
	print "\n";
}
