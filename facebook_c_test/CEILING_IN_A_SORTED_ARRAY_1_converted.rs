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
fn  f_gold  ( mut  arr  [  ] :i32 , mut  low :i32 , mut  high :i32 , mut  x :i32 )  -> i32{ 
let mut  mid :i32;
 if  x  <=  arr [ low ]{
 return  low ;
}
 if  x  >  arr [ high ]{
 return - 1 ;
}
 mid  = ( low  +  high ) / 2  as i32;
 if  arr [ mid ] ==  x {
 return  mid ;
}
 else {
 if  arr [ mid ] <  x { 
 if  mid  + 1  <=  high  &&  x  <=  arr [ mid  + 1 ]{
 return  mid  + 1 ;
}
 else {
 return  f_gold ( arr  , mid  + 1  , high  , x );
}
} 
 else { 
 if  mid  - 1  >=  low  &&  x  >  arr [ mid  - 1 ]{
 return  mid ;
}
 else {
 return  f_gold ( arr  , low  , mid  - 1  , x );
}
} 
}
} 
fn  f_filled  ( mut  arr  [  ] :i32 , mut  low :i32 , mut  high :i32 , mut  x :i32 )  -> i32{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0_0 : &[i32] = 2  ,6  ,13  ,16  ,23  ,24  ,24  ,27  ,30  ,32  ,34  ,34  ,55  ,56  ,56  ,63  ,66  ,81  ,83  ,96  as i32;
let mut  param0_1 : &[i32] = - 28  ,- 96  ,48  ,22  ,- 12  ,72  ,48  ,- 70  ,- 96  ,- 84  ,- 62  ,22  ,18  ,- 92  ,- 74  ,14  ,28  ,52  ,64  ,72  ,16  ,- 76  ,46  as i32;
let mut  param0_2 : &[i32] = 0  ,1  as i32;
let mut  param0_3 : &[i32] = 51  ,98  ,25  ,10  ,43  ,91  ,33  ,25  ,85  ,51  ,94  ,6  ,35  ,48  ,11  ,97  ,67  ,21  ,50  ,9  ,11  ,51  ,86  ,61  ,22  ,88  ,89  ,11  as i32;
let mut  param0_4 : &[i32] = - 94  ,- 92  ,- 88  ,- 74  ,- 52  ,- 50  ,- 48  ,- 44  ,- 40  ,- 36  ,- 32  ,- 26  ,20  ,22  ,30  ,32  ,46  ,56  ,56  ,60  ,62  ,64  ,80  ,84  ,86  ,94  ,96  ,96  as i32;
let mut  param0_5 : &[i32] = 1  ,0  ,0  ,1  ,1  ,0  ,0  ,1  ,0  ,1  ,0  ,1  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  as i32;
let mut  param0_6 : &[i32] = 4  ,5  ,5  ,13  ,26  ,40  ,46  ,51  ,58  ,60  ,64  ,66  ,68  ,69  ,71  ,74  ,78  ,81  ,83  ,88  ,88  ,90  ,98  ,99  as i32;
let mut  param0_7 : &[i32] = 92  ,6  ,- 54  ,84  ,- 10  ,32  ,50  ,40  ,- 38  ,64  ,- 64  ,- 10  ,70  ,- 68  ,- 6  ,- 16  ,68  ,34  ,- 66  ,- 82  ,84  ,98  ,50  ,82  ,78  ,4  ,34  ,- 34  ,78  ,64  ,32  ,58  ,- 94  ,40  ,50  ,0  ,- 92  ,- 36  ,10  ,- 54  ,58  ,- 78  ,- 88  ,32  ,6  as i32;
let mut  param0_8 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  as i32;
let mut  param0_9 : &[i32] = 80  ,67  ,30  ,35  ,9  as i32;
let mut // Handling Pointers...
*mut  param0 : [ i32;10 ] =  param0_0  , param0_1  , param0_2  , param0_3  , param0_4  , param0_5  , param0_6  , param0_7  , param0_8  , param0_9  as i32;
let mut  param1 : &[i32] = 13  ,11  ,1  ,20  ,20  ,15  ,12  ,23  ,24  ,2  as i32;
let mut  param2 : &[i32] = 11  ,18  ,1  ,20  ,15  ,17  ,17  ,28  ,17  ,3  as i32;
let mut  param3 : &[i32] = 18  ,21  ,1  ,15  ,15  ,22  ,14  ,28  ,22  ,2  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ] , param1 [ i ] , param2 [ i ] , param3 [ i ]) ==  f_gold ( param0 [ i ] , param1 [ i ] , param2 [ i ] , param3 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
