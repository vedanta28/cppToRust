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
fn  f_gold  ( mut  n :i32 )  -> i32{ 
let mut  bell : [  [ i32; n  + 1 ]; n  + 1 ];
 bell  = 1  as i32;
let mut  i :i32 = 1  as i32;
while  i  <=  n {
 bell  =  bell [ i  - 1 ][ i  - 1 ];
let mut  j :i32 = 1  as i32;
while  j  <=  i {
 bell  =  bell [ i  - 1 ][ j  - 1 ] +  bell [ i ][ j  - 1 ];
 j +=1 ;}
 i +=1 ;}
 return  bell [ n ][0 ];
} 
fn  f_filled  ( mut  n :i32 )  -> i32{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[i32] = 84  ,78  ,9  ,73  ,4  ,53  ,85  ,38  ,39  ,6  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ]) ==  f_gold ( param0 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
