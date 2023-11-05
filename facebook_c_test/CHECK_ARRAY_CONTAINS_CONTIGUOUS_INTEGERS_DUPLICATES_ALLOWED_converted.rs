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
let mut  max :i32 = *  max_element ( arr  , arr  +  n ) as i32;
let mut  min :i32 = *  min_element ( arr  , arr  +  n ) as i32;
let mut  m :i32 =  max  -  min  + 1  as i32;
 if  m  >  n {
 return false ;
}
let mut  visited : [ bool; m ];
 memset (  visited  ,false  ,mem::size_of_val(( visited )) ) as bool;
let mut  i :i32 = 0  as i32;
while  i  <  n {
 visited  = true ;
 i +=1 ;}
let mut  i :i32 = 0  as i32;
while  i  <  m {
 if  visited [ i ] == false {
 return false ;
}
 i +=1 ;}
 return true ;
} 
fn  f_filled  ( mut  arr  [  ] :i32 , mut  n :i32 )  -> bool{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0_0 : &[i32] = 2  ,4  ,19  ,25  ,65  ,72  ,75  ,83  ,90  ,92  as i32;
let mut  param0_1 : &[i32] = 46  ,2  ,28  ,- 44  ,74  ,- 36  ,- 8  ,30  ,- 96  ,60  ,52  ,- 58  ,16  ,- 38  ,78  ,38  ,- 28  ,16  ,26  ,- 42  ,48  ,40  ,6  ,72  as i32;
let mut  param0_2 : &[i32] = 0  ,1  ,1  ,1  as i32;
let mut  param0_3 : &[i32] = 50  ,21  ,9  ,29  ,86  ,2  ,82  ,49  ,34  ,18  ,77  ,83  ,44  ,67  ,85  ,58  ,15  ,85  ,22  ,3  ,39  ,67  ,42  ,37  ,6  ,35  ,18  ,57  ,41  ,32  ,39  ,30  ,41  ,68  ,84  ,36  ,64  ,36  as i32;
let mut  param0_4 : &[i32] = - 92  ,- 82  ,- 80  ,- 78  ,- 66  ,- 66  ,- 62  ,- 58  ,- 54  ,- 52  ,- 48  ,- 30  ,- 26  ,- 22  ,- 20  ,- 20  ,- 18  ,- 14  ,- 2  ,12  ,20  ,24  ,26  ,26  ,28  ,28  ,32  ,36  ,42  ,48  ,50  ,52  ,56  ,64  ,70  ,72  ,72  ,80  ,82  ,84  ,86  ,92  as i32;
let mut  param0_5 : &[i32] = 1  ,0  ,0  ,1  ,0  ,0  ,1  ,0  ,0  ,1  ,1  ,0  ,1  ,0  ,0  ,0  ,0  ,1  ,0  ,1  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,1  ,1  ,1  ,0  ,0  ,1  ,1  ,0  ,1  ,1  ,1  ,0  ,0  ,1  ,0  ,1  ,0  ,0  ,0  ,0  as i32;
let mut  param0_6 : &[i32] = 18  ,19  ,21  ,23  ,30  ,33  ,38  ,40  ,45  ,56  ,63  ,68  ,93  ,96  as i32;
let mut  param0_7 : &[i32] = 20  ,- 90  ,- 42  ,48  ,18  ,- 46  ,82  ,- 12  ,- 88  ,82  ,62  ,24  ,20  ,64  ,- 68  ,- 34  ,- 38  ,8  ,- 54  ,- 20  ,- 92  ,34  ,- 90  ,78  ,18  ,8  ,- 6  ,10  ,98  ,- 24  ,72  ,- 92  ,76  ,- 22  ,12  ,- 44  ,2  ,68  ,- 72  ,42  ,34  ,20  ,- 48  as i32;
let mut  param0_8 : &[i32] = 0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  as i32;
let mut  param0_9 : &[i32] = 81  ,25  ,50  ,48  ,35  ,38  ,49  ,21  ,47  ,94  ,94  ,55  ,23  ,45  ,92  ,23  ,93  ,33  ,64  ,9  ,90  ,64  ,81  ,17  ,2  ,73  ,8  ,7  ,35  ,36  ,72  as i32;
let mut // Handling Pointers...
*mut  param0 : [ i32;10 ] =  param0_0  , param0_1  , param0_2  , param0_3  , param0_4  , param0_5  , param0_6  , param0_7  , param0_8  , param0_9  as i32;
let mut  param1 : &[i32] = 8  ,14  ,2  ,23  ,26  ,43  ,8  ,34  ,8  ,27  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ] , param1 [ i ]) ==  f_gold ( param0 [ i ] , param1 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
