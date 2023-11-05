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
fn  f_gold  ( mut  arr  [  ] :i32 , mut  n :i32 , mut  x :i32 )  -> i32{ 
let mut  i :i32;
 i  = 0 ;
while  i  <  n {
 if  arr [ i ] ==  x {
 return  i ;
}
 i +=1 ;}
 return - 1 ;
} 
fn  f_filled  ( mut  arr  [  ] :i32 , mut  n :i32 , mut  x :i32 )  -> i32{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0_0 : &[i32] = 4  ,5  ,5  ,11  ,13  ,14  ,15  ,19  ,22  ,22  ,23  ,26  ,29  ,29  ,36  ,44  ,48  ,49  ,65  ,65  ,67  ,68  ,70  ,76  ,79  ,79  ,81  ,85  ,88  ,91  ,91  ,92  ,92  ,97  as i32;
let mut  param0_1 : &[i32] = - 24  ,- 78  ,- 32  ,- 48  ,0  ,4  ,- 42  as i32;
let mut  param0_2 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  as i32;
let mut  param0_3 : &[i32] = 38  ,14  ,75  ,16  ,91  ,11  ,98  ,43  ,67  ,9  ,21  ,10  ,82  ,72  ,32  ,81  ,48  ,60  ,2  ,91  ,10  ,90  ,12  ,83  as i32;
let mut  param0_4 : &[i32] = - 92  ,- 92  ,- 82  ,- 80  ,- 76  ,- 66  ,- 64  ,- 64  ,- 56  ,- 48  ,- 38  ,- 38  ,- 34  ,- 32  ,- 32  ,- 10  ,- 8  ,- 6  ,- 2  ,0  ,8  ,10  ,18  ,20  ,22  ,22  ,30  ,34  ,38  ,38  ,38  ,44  ,50  ,52  ,56  ,64  ,64  ,66  ,70  ,76  ,88  as i32;
let mut  param0_5 : &[i32] = 0  ,1  ,1  ,0  ,0  ,1  ,1  ,0  ,0  ,0  ,1  ,1  ,1  ,1  as i32;
let mut  param0_6 : &[i32] = 1  ,4  ,4  ,4  ,4  ,8  ,12  ,13  ,14  ,14  ,22  ,25  ,25  ,27  ,29  ,33  ,36  ,38  ,40  ,40  ,40  ,41  ,47  ,47  ,47  ,48  ,48  ,50  ,51  ,52  ,52  ,52  ,55  ,56  ,59  ,59  ,62  ,64  ,66  ,77  ,82  ,84  ,90  ,91  ,91  ,93  as i32;
let mut  param0_7 : &[i32] = - 90  ,- 60  ,- 58  ,- 72  ,92  ,54  ,- 32  ,- 70  ,- 94  ,18  ,64  ,- 90  ,- 90  ,- 56  ,82  ,- 14  ,- 74  ,- 96  ,- 90  ,- 8  ,- 48  ,76  ,- 28  ,10  ,- 52  ,- 8  ,- 46  ,- 32  ,82  ,46  ,58  ,92  ,4  ,48  ,- 96  ,- 66  ,60  ,60  ,62  ,- 68  as i32;
let mut  param0_8 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  as i32;
let mut  param0_9 : &[i32] = 42  ,17  ,77  ,96  ,72  ,36  ,74  ,97  ,7  ,94  ,80  ,7  ,27  ,58  ,49  ,81  ,51  ,9  as i32;
let mut // Handling Pointers...
*mut  param0 : [ i32;10 ] =  param0_0  , param0_1  , param0_2  , param0_3  , param0_4  , param0_5  , param0_6  , param0_7  , param0_8  , param0_9  as i32;
let mut  param1 : &[i32] = 17  ,4  ,6  ,17  ,25  ,11  ,38  ,22  ,8  ,16  as i32;
let mut  param2 : &[i32] = 5  ,0  ,0  ,75  ,25  ,- 1  ,4  ,22  ,8  ,11  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ] , param1 [ i ] , param2 [ i ]) ==  f_gold ( param0 [ i ] , param1 [ i ] , param2 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
