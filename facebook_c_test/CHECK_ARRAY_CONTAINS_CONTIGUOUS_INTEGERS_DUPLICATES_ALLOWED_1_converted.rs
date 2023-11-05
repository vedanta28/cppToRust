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
let mut  us : // Templates are yet to supported! Currently copying them as it is!
 unordered_set<int> ;
let mut  i :i32 = 0  as i32;
while  i  <  n {
 us . insert ( arr [ i ]);
 i +=1 ;}
let mut  count :i32 = 1  as i32;
let mut  curr_ele :i32 =  arr [0 ] - 1  as i32;
 while  us . find ( curr_ele ) !=  us . end (){ 
 count +=1 ;
 curr_ele -=1 ;
} 
 curr_ele  =  arr [0 ] + 1 ;
 while  us . find ( curr_ele ) !=  us . end (){ 
 count +=1 ;
 curr_ele +=1 ;
} 
 return ( count  == ( len ( us )) as i32);
} 
fn  f_filled  ( mut  arr  [  ] :i32 , mut  n :i32 )  -> bool{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0_0 : &[i32] = 15  ,19  ,38  ,59  ,71  as i32;
let mut  param0_1 : &[i32] = - 20  ,66  ,- 22  ,- 56  ,- 6  ,94  ,70  ,- 80  ,24  ,- 26  ,- 58  ,- 76  ,- 20  ,- 8  ,- 62  ,18  ,- 56  ,- 20  ,42  ,- 40  ,- 88  ,- 74  ,64  ,- 26  ,- 92  ,66  ,- 18  ,- 64  ,66  ,12  ,24  ,- 8  ,78  ,- 82  ,14  ,- 76  as i32;
let mut  param0_2 : &[i32] = 0  ,0  ,1  ,1  ,1  as i32;
let mut  param0_3 : &[i32] = 40  ,38  ,17  ,50  ,16  ,35  ,34  ,23  ,3  ,12  ,97  ,53  ,75  ,36  ,3  ,73  ,99  ,11  ,70  ,9  ,23  ,3  ,11  ,9  ,64  ,44  ,62  ,94  ,55  ,69  ,44  ,59  ,57  ,99  ,69  ,12  ,27  ,42  ,14  ,83  ,53  ,4  ,4  as i32;
let mut  param0_4 : &[i32] = - 78  ,- 36  ,- 28  ,- 16  ,- 8  ,- 4  ,4  ,4  ,10  ,14  ,30  ,30  ,32  ,32  ,38  ,46  ,54  ,72  as i32;
let mut  param0_5 : &[i32] = 1  ,0  ,1  ,0  ,0  ,1  ,1  ,0  ,0  ,1  ,1  ,1  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,0  ,1  ,1  ,0  ,1  ,1  as i32;
let mut  param0_6 : &[i32] = 7  ,32  ,54  ,70  ,79  ,88  as i32;
let mut  param0_7 : &[i32] = - 38  ,48  ,- 96  ,- 84  ,10  ,70  ,- 28  ,- 66  ,40  ,- 26  ,- 24  ,- 8  ,28  ,- 6  ,6  ,- 14  ,- 2  ,- 58  ,- 6  ,- 14  ,- 58  ,- 74  ,20  ,32  ,98  ,- 24  ,- 10  ,42  ,- 4  ,- 96  ,- 56  ,- 40  ,74  ,- 98  ,- 86  ,- 94  ,12  ,80  ,10  ,- 54  ,- 44  as i32;
let mut  param0_8 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  as i32;
let mut  param0_9 : &[i32] = 49  ,87  ,18  ,19  ,56  ,25  ,64  ,94  ,43  ,97  ,74  ,79  ,13  ,36  ,72  ,46  ,10  ,84  ,2  ,11  ,41  ,87  ,55  ,38  ,89  ,92  ,65  ,57  ,62  ,16  as i32;
let mut // Handling Pointers...
*mut  param0 : [ i32;10 ] =  param0_0  , param0_1  , param0_2  , param0_3  , param0_4  , param0_5  , param0_6  , param0_7  , param0_8  , param0_9  as i32;
let mut  param1 : &[i32] = 3  ,26  ,4  ,26  ,16  ,38  ,5  ,30  ,12  ,21  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ] , param1 [ i ]) ==  f_gold ( param0 [ i ] , param1 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
