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
let mut  volume :f64 = ( pow ( side  ,3 ) / (6  *  sqrt (2 ))) as f64;
 return  volume ;
} 
fn  f_filled  ( mut  side :i32 )  -> f64{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[i32] = 58  ,56  ,35  ,99  ,13  ,45  ,40  ,92  ,7  ,13  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  abs (1  - (0.0000001  +  abs ( f_gold ( param0 [ i ]))) / ( abs ( f_filled ( param0 [ i ])) + 0.0000001 )) < 0.001 { 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
