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
 if  n  == 0  ||  n  == 1 {
 return true ;
}
let mut  i :i32 = 1  as i32;
while  i  <  n {
 if  arr [ i  - 1 ] >  arr [ i ]{
 return false ;
}
 i +=1 ;}
 return true ;
} 
fn  f_filled  ( mut  arr  [  ] :i32 , mut  n :i32 )  -> bool{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0_0 : &[i32] = 2  ,3  ,4  ,10  ,11  ,13  ,17  ,19  ,23  ,26  ,28  ,29  ,30  ,34  ,35  ,37  ,38  ,38  ,43  ,49  ,49  ,50  ,52  ,53  ,55  ,55  ,57  ,58  ,58  ,59  ,64  ,66  ,67  ,70  ,72  ,72  ,75  ,77  ,77  ,87  ,89  ,89  ,90  ,91  ,98  ,99  ,99  ,99  as i32;
let mut  param0_1 : &[i32] = 56  ,- 94  ,- 26  ,- 52  ,58  ,- 66  ,- 52  ,- 66  ,- 94  ,44  ,38  ,- 66  ,70  ,- 70  ,- 80  ,- 78  ,- 72  ,- 60  ,- 76  ,68  ,- 50  ,32  ,- 16  ,84  ,74  ,- 42  ,98  ,- 8  ,72  ,26  ,24  ,6  ,24  ,86  ,86  ,78  ,- 92  ,80  ,32  ,- 74  ,26  ,50  ,92  ,4  ,2  ,- 34  ,- 2  ,- 18  ,- 10  as i32;
let mut  param0_2 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  as i32;
let mut  param0_3 : &[i32] = 38  ,79  ,76  ,92  ,92  as i32;
let mut  param0_4 : &[i32] = - 42  ,- 28  ,2  ,32  ,50  ,56  ,86  ,96  ,98  as i32;
let mut  param0_5 : &[i32] = 1  ,0  ,0  ,1  ,1  ,1  ,0  ,1  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  as i32;
let mut  param0_6 : &[i32] = 1  ,9  ,12  ,21  ,21  ,24  ,34  ,55  ,60  ,63  ,67  ,68  ,88  ,89  ,91  ,94  ,98  ,99  as i32;
let mut  param0_7 : &[i32] = - 96  ,96  ,- 98  ,- 42  ,- 74  ,40  ,42  ,50  ,- 46  ,- 52  ,8  ,- 46  ,48  ,88  ,- 78  ,- 72  ,- 10  ,- 20  ,98  ,- 40  ,- 18  ,36  ,4  ,46  ,52  ,28  ,- 88  ,- 28  ,- 28  ,- 86  as i32;
let mut  param0_8 : &[i32] = 0  ,0  ,0  ,0  ,1  ,1  as i32;
let mut  param0_9 : &[i32] = 66  ,12  ,48  ,82  ,33  ,77  ,99  ,98  ,14  ,92  as i32;
let mut // Handling Pointers...
*mut  param0 : [ i32;10 ] =  param0_0  , param0_1  , param0_2  , param0_3  , param0_4  , param0_5  , param0_6  , param0_7  , param0_8  , param0_9  as i32;
let mut  param1 : &[i32] = 46  ,30  ,13  ,2  ,7  ,11  ,9  ,29  ,3  ,7  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ] , param1 [ i ]) ==  f_gold ( param0 [ i ] , param1 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
