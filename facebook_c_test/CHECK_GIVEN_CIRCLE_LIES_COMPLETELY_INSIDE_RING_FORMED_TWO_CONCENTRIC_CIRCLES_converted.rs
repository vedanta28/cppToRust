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
fn  f_gold  ( mut  r :i32 , mut  R :i32 , mut  r1 :i32 , mut  x1 :i32 , mut  y1 :i32 )  -> bool{ 
let mut  dis :i32 =  sqrt ( x1  *  x1  +  y1  *  y1 ) as i32;
 return ( dis  -  r1  >=  R  &&  dis  +  r1  <=  r );
} 
fn  f_filled  ( mut  r :i32 , mut  R :i32 , mut  r1 :i32 , mut  x1 :i32 , mut  y1 :i32 )  -> bool{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[i32] = 8  ,400  ,1  ,61  ,60  ,88  ,60  ,26  ,33  ,70  as i32;
let mut  param1 : &[i32] = 4  ,1  ,400  ,40  ,49  ,10  ,79  ,88  ,65  ,57  as i32;
let mut  param2 : &[i32] = 2  ,10  ,10  ,2  ,68  ,69  ,92  ,75  ,57  ,77  as i32;
let mut  param3 : &[i32] = 6  ,74  ,74  ,50  ,77  ,71  ,29  ,84  ,21  ,52  as i32;
let mut  param4 : &[i32] = 0  ,38  ,38  ,0  ,71  ,26  ,38  ,10  ,61  ,87  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ] , param1 [ i ] , param2 [ i ] , param3 [ i ] , param4 [ i ]) ==  f_gold ( param0 [ i ] , param1 [ i ] , param2 [ i ] , param3 [ i ] , param4 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
