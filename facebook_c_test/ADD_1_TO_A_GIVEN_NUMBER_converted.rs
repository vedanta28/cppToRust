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
fn  f_gold  ( mut  x :i32 )  -> i32{ 
let mut  m :i32 = 1  as i32;
 while  x  &  m { 
 x  =  x  ^  m ;
 m  <<= 1 ;
} 
 x  =  x  ^  m ;
 return  x ;
} 
fn  f_filled  ( mut  x :i32 )  -> i32{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[i32] = 96  ,66  ,67  ,13  ,75  ,78  ,1  ,83  ,27  ,65  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ]) ==  f_gold ( param0 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
