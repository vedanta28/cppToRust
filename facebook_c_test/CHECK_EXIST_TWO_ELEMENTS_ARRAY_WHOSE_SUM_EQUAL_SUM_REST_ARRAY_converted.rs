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
fn  f_gold  ( mut  arr  [  ] :i32 , mut  n :i32 )  -> bool{ 
let mut  sum :i32 = 0  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  n {
 sum  +=  arr [ i ];
 i +=1 ;}
 if  sum  % 2  != 0 {
 return false ;
}
 sum  =  sum  / 2 ;
let mut  s : // Templates are yet to supported! Currently copying them as it is!
 unordered_set<int> ;
let mut  i :i32 = 0  as i32;
while  i  <  n {
let mut  val :i32 =  sum  -  arr [ i ] as i32;
 if  s . find ( val ) !=  s . end (){ 
 println! ( "Pair elements are {} and {}\n"  , arr [ i ] , val  );
 return true ;
} 
 s . insert ( arr [ i ]);
 i +=1 ;}
 return false ;
} 
fn  f_filled  ( mut  arr  [  ] :i32 , mut  n :i32 )  -> bool{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0_0 : &[i32] = 15  as i32;
let mut  param0_1 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  as i32;
let mut  param0_2 : &[i32] = 69  ,6  ,24  ,30  ,75  ,37  ,61  ,76  ,19  ,18  ,90  ,9  ,49  ,24  ,58  ,97  ,18  ,85  ,24  ,93  ,71  ,98  ,92  ,59  ,75  ,75  ,75  ,70  ,35  ,58  ,50  ,1  ,64  ,66  ,33  as i32;
let mut  param0_3 : &[i32] = - 94  ,- 94  ,- 92  ,- 74  ,- 60  ,- 58  ,- 56  ,- 44  ,- 42  ,- 40  ,- 28  ,- 14  ,2  ,4  ,14  ,20  ,24  ,28  ,40  ,42  ,42  ,66  ,78  ,78  ,80  ,82  ,96  as i32;
let mut  param0_4 : &[i32] = 1  ,0  ,1  ,1  ,0  ,0  ,1  ,1  ,0  ,0  ,1  ,1  ,0  ,1  as i32;
let mut  param0_5 : &[i32] = 21  ,26  ,26  ,27  ,61  ,62  ,96  as i32;
let mut  param0_6 : &[i32] = - 54  ,86  ,20  ,26  as i32;
let mut  param0_7 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  as i32;
let mut  param0_8 : &[i32] = 44  ,35  ,26  ,15  ,56  ,6  ,36  ,53  ,15  ,66  ,20  ,53  ,99  ,96  ,51  ,12  ,61  ,19  ,79  ,40  ,99  ,42  ,86  ,8  ,11  ,54  ,93  ,46  ,23  ,47  ,41  ,26  ,66  ,5  ,86  ,52  ,64  ,51  ,4  ,21  ,63  ,14  ,7  ,53  ,31  ,8  ,9  ,63  as i32;
let mut // Handling Pointers...
*mut  param0 : [ i32;9 ] =  param0_0  , param0_1  , param0_2  , param0_3  , param0_4  , param0_5  , param0_6  , param0_7  , param0_8  as i32;
let mut  param1 : &[i32] = 6  ,6  ,13  ,18  ,26  ,10  ,6  ,3  ,4  ,31  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ] , param1 [ i ]) ==  f_gold ( param0 [ i ] , param1 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
