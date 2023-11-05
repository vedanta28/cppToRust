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
fn  f_gold  ( mut  str  [  ] :char )  -> bool{ 
let mut  list : // Templates are yet to supported! Currently copying them as it is!
 vector<char> ;
let mut  i :i32 = 0  as i32;
while  i  <  strlen ( str ){
let mut  pos   =  find ( list . begin () , list . end () , str [ i ]);
 if  pos  !=  list . end (){ 
let mut  posi   =  find ( list . begin () , list . end () , str [ i ]);
 list . erase ( posi );
} 
 else {
 list . push_back ( str [ i ]);
}
 i +=1 ;}
 if  strlen ( str ) % 2  == 0  &&  list . empty () || ( strlen ( str ) % 2  == 1  &&  len ( list ) == 1 ){
 return true ;
}
 else {
 return false ;
}
} 
fn  f_filled  ( mut  str  [  ] :char )  -> bool{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[ [ char;100 ]] = "abccba"  ,"2674377254"  ,"11"  ,"abcdecba"  ,"26382426486138"  ,"111010111010"  ,"hUInqJXNdbfP"  ,"5191"  ,"1110101101"  ,"NupSrU xz"  as char;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ]) ==  f_gold ( param0 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
