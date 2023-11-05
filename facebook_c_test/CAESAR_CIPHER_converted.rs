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
fn  f_gold  [  ]  ( mut  text  [  ] :char , mut  s :i32 )  -> char{ 
let mut  result : &[char] = ""  as char;
let mut  i :i32 = 0  as i32;
while  i  <  strlen ( text ){
 if  isupper ( text [ i ]){
 result  += (( text [ i ] +  s  - 65 ) % 26  + 65 );
}
 else {
 result  += (( text [ i ] +  s  - 97 ) % 26  + 97 );
}
 i +=1 ;}
 return  result ;
} 
fn  f_filled  [  ]  ( mut  text  [  ] :char , mut  s :i32 )  -> char{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[ [ char;100 ]] = "LsvbpcviVPwq"  ,"35225904"  ,"010010"  ,"QnYd"  ,"2571694"  ,"101101011010"  ,"jb"  ,"928874"  ,"11"  ,"FbvbkMb"  as char;
let mut  param1 : &[i32] = 15  ,2  ,36  ,44  ,11  ,94  ,22  ,83  ,93  ,37  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ] , param1 [ i ]) ==  f_gold ( param0 [ i ] , param1 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
