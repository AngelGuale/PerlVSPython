use Tie::File;

tie @array, 'Tie::File', "patronesFile.txt" or die;


for my $i (0 .. $#array)
{
      print($array[$i]);
}