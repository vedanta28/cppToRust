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
fn  f_gold  ( mut  N  [  ] :char )  -> i32{ 
let mut  len :i32 =  strlen ( N ) as i32;
let mut  l :i32 = ( len ) / 2  as i32;
let mut  count :i32 = 0  as i32;
let mut  i :i32 = 1  as i32;
while  i  <=  l {
let mut  s : &[char] =  N . substr (0  , i ) as char;
let mut  l1 :i32 =  strlen ( s ) as i32;
let mut  t : &[char] =  N . substr ( i  , l1 ) as char;
 if  s [0 ] == '0'  ||  t [0 ] == '0' {
 continue;
 }
 if  s . compare ( t ) == 0 {
 count +=1 ;
}
 i +=1 ;}
 return  count ;
} 
fn  f_filled  ( mut  N  [  ] :char )  -> i32{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[ [ char;100 ]] = "ZCoQhuM"  ,"2674377254"  ,"11"  ,"LbuGlvRyWAPBpo"  ,"26382426486138"  ,"111010111010"  ,"hUInqJXNdbfP"  ,"5191"  ,"1110101101"  ,"2202200"  as char;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ]) ==  f_gold ( param0 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
