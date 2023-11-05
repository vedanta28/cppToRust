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
fn  f_gold  ( mut  s :f64 )  -> f64{ 
 return ((3  *  sqrt (3 ) * ( s  *  s )) / 2 );
} 
fn  f_filled  ( mut  s :f64 )  -> f64{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[f64] = 1772.6589509256596  ,- 599.737107809315  ,1074.1765931782  ,- 1182.4087746714795  ,8083.035797247716  ,- 6126.414356565494  ,5370.057504189614  ,- 6947.020794285176  ,2110.5107873533325  ,- 6458.751326919488  as f64;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  abs (1  - (0.0000001  +  abs ( f_gold ( param0 [ i ]))) / ( abs ( f_filled ( param0 [ i ])) + 0.0000001 )) < 0.001 { 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
