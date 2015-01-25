
  use Benchmark qw(:all) ;
   use Benchmark qw( :hireswallclock ) ;
     use Time::HiRes qw(time);
   $t0 = time;
   for(my $i=0;$i<100;$i=$i+1){
  #print "iteracion\n";
  
  }
   $elapsed = time - $t0;
   print "Tiempo: $elapsed ";
  
  timethis(1, ' for(my $i=0;$i<100;$i=$i+1){
  #print "iteracion\n";
  
  }');
  
 #  use Time::HiRes qw( usleep ualarm gettimeofday tv_interval nanosleep
   #                   clock_gettime clock_getres clock_nanosleep clock
    #                  stat lstat );
  $count=1;
  $code='
  $a=0;
  $b=1;
  $c=2;
  if($b>$a){
  
  if($c>$b){
  
  for(my $i=0;$i<100;$i=$i+1){
  #print "iteracion\n";
  $a=$b+$c;
  $c=$a-$b;
  }
  }
  
  }
  
  ';
  timethis ($count, $code);
