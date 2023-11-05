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
fn  f_gold  ( mut  side :i32 )  -> f64{ 
 return (((15  + (7  * ( sqrt (5 )))) / 4 ) * ( pow ( side  ,3 )));
} 
fn  f_filled  ( mut  side :i32 )  -> f64{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[i32] = 56  ,73  ,22  ,10  ,84  ,20  ,51  ,91  ,10  ,83  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  abs (1  - (0.0000001  +  abs ( f_gold ( param0 [ i ]))) / ( abs ( f_filled ( param0 [ i ])) + 0.0000001 )) < 0.001 { 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
