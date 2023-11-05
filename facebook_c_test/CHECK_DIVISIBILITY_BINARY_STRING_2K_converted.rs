#![allow(warnings, unused)]
fn  min  ( mut  x :i32 , mut  y :i32 )  -> i32{ 
 return  if ( x  <  y ) {  x  }  else {  y  } ;
} 
fn  max  ( mut  x :i32 , mut  y :i32 )  -> i32{ 
 return  if ( x  >  y ) {  x  }  else {  y  } ;
} 
fn  cmpfunc  ( mut // Handling Pointers...
*mut  a :  , mut // Handling Pointers...
*mut  b :  )  -> i32{ 
 return ;
;
;
;
let mut // Handling Pointers...
*mut  a :i32;
;
;
;
 b  as int**mut ;
} 
fn  len  ( mut  arr  [  ] :i32 )  -> i32{ 
 return ((mem::size_of_val(( arr )) / mem::size_of_val(( arr )[0 ])) as i32);
} 
fn  sort  ( mut  arr  [  ] :i32 , mut  n :i32 )  { 
 qsort (  arr  , n  ,mem::size_of_val(i32) , cmpfunc  ) as i32;
} 
fn  f_gold  ( mut  str  [  ] :char , mut  k :i32 )  -> bool{ 
let mut  n :i32 =  strlen ( str ) as i32;
let mut  c :i32 = 0  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  k {
 if  str [ n  -  i  - 1 ] == '0' {
 c +=1 ;
}
 i +=1 ;}
 return ( c  ==  k );
} 
fn  f_filled  ( mut  str  [  ] :char , mut  k :i32 )  -> bool{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[ [ char;100 ]] = "111010100"  ,"111010100"  ,"111010100"  ,"111010000"  ,"111010000"  ,"10110001"  ,"tPPdXrYQSI"  ,"58211787"  ,"011"  ,"IkSMGqgzOrteVO"  as char;
let mut  param1 : &[i32] = 2  ,2  ,4  ,3  ,4  ,1  ,61  ,73  ,88  ,23  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled (&  param0 [ i ]. front () , param1 [ i ]) ==  f_gold (&  param0 [ i ]. front () , param1 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
