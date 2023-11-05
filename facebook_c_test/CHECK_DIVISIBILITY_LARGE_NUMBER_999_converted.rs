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
fn  f_gold  ( mut  num  [  ] :char )  -> bool{ 
let mut  n :i32 =  strlen ( num ) as i32;
 if  n  == 0  &&  num [0 ] == '0' {
 return true ;
}
 if  n  % 3  == 1 {
 num  = "00"  +  num ;
}
 if  n  % 3  == 2 {
 num  = "0"  +  num ;
}
let mut  gSum :i32 = 0  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  n {
let mut  group :i32 = 0  as i32;
 group  += ( num [ i +=1 ] - '0' ) * 100 ;
 group  += ( num [ i +=1 ] - '0' ) * 10 ;
 group  +=  num [ i ] - '0' ;
 gSum  +=  group ;
 i +=1 ;}
 if  gSum  > 1000 { 
 num  =  to_string ( gSum );
 n  =  strlen ( num );
 gSum  =  f_gold ( num );
} 
 return ( gSum  == 999 );
} 
fn  f_filled  ( mut  num  [  ] :char )  -> bool{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[ [ char;100 ]] = "235764"  ,"321308924"  ,"101111"  ,"1998"  ,"339589"  ,"0000101"  ,"264735"  ,"19570453184"  ,"000"  ,"SsHh"  as char;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ]) ==  f_gold ( param0 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
