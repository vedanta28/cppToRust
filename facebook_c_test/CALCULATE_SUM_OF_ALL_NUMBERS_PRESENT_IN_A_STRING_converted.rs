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
fn  f_gold  ( mut  str  [  ] :char )  -> i32{ 
let mut  temp : &[char] = ""  as char;
let mut  sum :i32 = 0  as i32;
// Will deal with for Range Declarations and Initializers later
for char ch  in  str { 
 if  isdigit ( ch ){
 temp  +=  ch ;
}
 else { 
 sum  +=  atoi ( temp . c_str ());
 temp  = ""  as char;
} 
} 
 return  sum  +  atoi ( temp . c_str ());
} 
fn  f_filled  ( mut  str  [  ] :char )  -> i32{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[ [ char;100 ]] = "FpuZdXbJ"  ,"8248545127035"  ,"00101111101"  ,"WuaZuohxsww"  ,"77298"  ,"101110"  ,"HiHCWcmzqGMdE"  ,"9661651"  ,"000110100111"  ,"nwuNyyVBJFWvO"  as char;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ]) ==  f_gold ( param0 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
