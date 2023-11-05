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
fn  f_gold  ( mut  p :f64 )  -> i32{ 
 return  ceil ( sqrt (2  * 365  *  log (1  / (1  -  p ))));
} 
fn  f_filled  ( mut  p :f64 )  -> i32{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[f64] = 0.9303713975220877  ,0.48126843587453595  ,0.48776789524757905  ,0.35184405927337793  ,0.8000415444743662  ,0.3528645948885943  ,0.33594265260473667  ,0.3603861267753616  ,7218.247044923335  ,- 4701.904717953173  as f64;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  abs (1  - (0.0000001  +  abs ( f_gold ( param0 [ i ]))) / ( abs ( f_filled ( param0 [ i ])) + 0.0000001 )) < 0.001 { 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
