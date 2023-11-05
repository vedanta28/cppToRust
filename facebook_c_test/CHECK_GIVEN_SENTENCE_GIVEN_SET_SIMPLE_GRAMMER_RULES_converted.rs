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
let mut  len :i32 =  strlen ( str ) as i32;
 if  str [0 ] < 'A'  ||  str [0 ] > 'Z' {
 return false ;
}
 if  str [ len  - 1 ] != '.' {
 return false ;
}
let mut  prev_state :i32 = 0  as i32;
let mut  curr_state :i32 = 0  as i32;
let mut  index :i32 = 1  as i32;
 while  str [ index ]{ 
 if  str [ index ] >= 'A'  &&  str [ index ] <= 'Z' {
 curr_state  = 0 ;
}
 else {
 if  str [ index ] == ' ' {
 curr_state  = 1 ;
}
 else {
 if  str [ index ] >= 'a'  &&  str [ index ] <= 'z' {
 curr_state  = 2 ;
}
 else {
 if  str [ index ] == '.' {
 curr_state  = 3 ;
}
}
}
}
 if  prev_state  ==  curr_state  &&  curr_state  != 2 {
 return false ;
}
 if  prev_state  == 2  &&  curr_state  == 0 {
 return false ;
}
 if  curr_state  == 3  &&  prev_state  != 1 {
 return ( str [ index  + 1 ] == '\0' );
}
 index +=1 ;
 prev_state  =  curr_state ;
} 
 return false ;
} 
fn  f_filled  ( mut  str  [  ] :char )  -> bool{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[ [ char;100 ]] = "I love cinema."  ,"The vertex is S."  ,"I am single."  ,"My name is KG."  ,"I lovE cinema."  ,"GeeksQuiz. is a quiz site."  ,"I love Geeksquiz and Geeksforgeeks."  ,"  You are my friend."  ,"I love cinema"  ,"Hello world !"  as char;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled (&  param0 [ i ]. front ()) ==  f_gold (&  param0 [ i ]. front ()){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
