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
fn  f_gold  ( mut  a  [  ] :i32 , mut  n :i32 , mut  k :i32 )  -> i32{ 
 if  k  >=  n  - 1 {
 return  n ;
}
let mut  best :i32 = 0  as i32;
let mut  times :i32 = 0  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  n {
 if  a [ i ] >  best { 
 best  =  a [ i ];
 if  i {
 times  = 1 ;
}
} 
 else {
 times  += 1 ;
}
 if  times  >=  k {
 return  best ;
}
 i +=1 ;}
 return  best ;
} 
fn  f_filled  ( mut  a  [  ] :i32 , mut  n :i32 , mut  k :i32 )  -> i32{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0_0 : &[i32] = 2  ,5  ,5  ,9  ,10  ,10  ,11  ,14  ,23  ,27  ,31  ,32  ,33  ,33  ,33  ,37  ,39  ,41  ,41  ,42  ,42  ,43  ,47  ,60  ,61  ,68  ,73  ,73  ,73  ,78  ,80  ,80  ,82  ,83  ,86  ,87  ,89  ,92  ,94  ,98  as i32;
let mut  param0_1 : &[i32] = 80  ,- 58  ,64  ,48  ,- 16  ,60  ,- 50  ,- 52  ,62  ,- 86  ,- 96  ,52  ,26  ,- 30  ,14  as i32;
let mut  param0_2 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  as i32;
let mut  param0_3 : &[i32] = 90  ,23  ,43  ,42  ,7  ,71  ,79  as i32;
let mut  param0_4 : &[i32] = - 96  ,- 96  ,- 90  ,- 84  ,- 68  ,- 64  ,- 56  ,- 56  ,- 50  ,- 50  ,- 48  ,- 46  ,- 28  ,- 18  ,0  ,0  ,6  ,32  ,32  ,34  ,42  ,42  ,46  ,50  ,50  ,52  ,64  ,64  ,70  ,76  ,84  ,88  as i32;
let mut  param0_5 : &[i32] = 1  ,1  ,1  as i32;
let mut  param0_6 : &[i32] = 2  ,9  ,15  ,19  ,26  ,29  ,42  ,45  ,46  ,47  ,55  ,60  ,60  ,61  ,62  ,64  ,68  ,69  ,74  ,79  ,96  as i32;
let mut  param0_7 : &[i32] = - 32  ,12  ,80  ,42  ,80  ,8  ,58  ,- 76  ,- 42  ,- 98  ,22  ,- 90  ,- 16  ,- 4  ,- 62  ,- 32  ,28  ,12  ,78  ,- 52  ,- 84  ,78  ,88  ,- 76  ,- 52  ,68  ,- 34  ,- 16  ,- 4  ,2  ,- 78  ,- 94  ,- 22  ,34  ,6  ,- 62  ,72  as i32;
let mut  param0_8 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  as i32;
let mut  param0_9 : &[i32] = 52  ,19  as i32;
let mut // Handling Pointers...
*mut  param0 : [ i32;10 ] =  param0_0  , param0_1  , param0_2  , param0_3  , param0_4  , param0_5  , param0_6  , param0_7  , param0_8  , param0_9  as i32;
let mut  param1 : &[i32] = 33  ,14  ,7  ,4  ,28  ,1  ,14  ,26  ,26  ,1  as i32;
let mut  param2 : &[i32] = 37  ,13  ,6  ,4  ,21  ,2  ,17  ,31  ,14  ,1  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ] , param1 [ i ] , param2 [ i ]) ==  f_gold ( param0 [ i ] , param1 [ i ] , param2 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
