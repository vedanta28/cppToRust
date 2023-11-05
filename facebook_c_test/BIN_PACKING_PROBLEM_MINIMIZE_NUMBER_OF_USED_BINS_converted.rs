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
fn  f_gold  ( mut  weight  [  ] :i32 , mut  n :i32 , mut  c :i32 )  -> i32{ 
let mut  res :i32 = 0  as i32;
let mut  bin_rem :i32 =  c  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  n {
 if  weight [ i ] >  bin_rem { 
 res +=1 ;
 bin_rem  =  c  -  weight [ i ];
} 
 else {
 bin_rem  -=  weight [ i ];
}
 i +=1 ;}
 return  res ;
} 
fn  f_filled  ( mut  weight  [  ] :i32 , mut  n :i32 , mut  c :i32 )  -> i32{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0_0 : &[i32] = 6  ,12  ,14  ,16  ,19  ,24  ,29  ,31  ,33  ,34  ,41  ,43  ,47  ,53  ,53  ,59  ,64  ,70  ,70  ,71  ,72  ,73  ,74  ,80  ,81  ,89  ,90  as i32;
let mut  param0_1 : &[i32] = - 88  ,- 26  ,70  ,- 92  ,96  ,84  ,- 24  ,- 18  ,84  ,62  ,- 72  ,42  ,72  ,2  ,30  ,86  as i32;
let mut  param0_2 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  as i32;
let mut  param0_3 : &[i32] = 51  ,7  ,6  ,24  ,19  ,83  ,9  ,36  ,40  ,93  ,24  ,48  ,63  ,69  ,53  ,54  ,42  ,45  ,90  ,14  ,29  ,6  ,7  ,37  ,53  ,18  ,87  ,38  ,59  ,1  ,68  ,44  ,47  ,35  ,87  ,91  ,60  ,90  ,52  ,8  ,80  ,41  ,3  ,96  as i32;
let mut  param0_4 : &[i32] = - 98  ,- 90  ,- 78  ,- 48  ,- 36  ,- 20  ,2  ,8  ,16  ,40  ,54  ,54  ,60  ,92  as i32;
let mut  param0_5 : &[i32] = 1  ,1  ,1  ,1  ,0  ,0  ,1  ,1  ,0  ,0  ,1  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,1  ,0  ,1  ,0  ,1  ,1  ,0  ,1  ,1  ,1  ,1  ,1  ,0  ,1  ,1  ,0  ,0  ,1  ,0  ,0  ,0  ,0  as i32;
let mut  param0_6 : &[i32] = 8  ,14  ,16  ,35  ,40  ,45  ,54  ,57  ,58  ,59  ,87  ,88  ,93  ,95  ,97  as i32;
let mut  param0_7 : &[i32] = - 46  ,- 6  ,60  ,- 88  ,10  ,94  ,- 12  ,- 64  ,- 68  ,- 76  ,- 60  ,- 10  ,28  ,18  ,86  ,88  ,80  ,- 56  ,94  ,- 6  ,- 42  ,72  ,- 10  ,54  ,- 82  ,- 52  ,- 70  ,- 28  ,- 74  ,82  ,- 12  ,42  ,44  ,56  ,52  ,- 28  ,22  ,62  ,- 20  as i32;
let mut  param0_8 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  as i32;
let mut  param0_9 : &[i32] = 48  ,57  ,21  ,82  ,99  as i32;
let mut // Handling Pointers...
*mut  param0 : [ i32;10 ] =  param0_0  , param0_1  , param0_2  , param0_3  , param0_4  , param0_5  , param0_6  , param0_7  , param0_8  , param0_9  as i32;
let mut  param1 : &[i32] = 21  ,11  ,27  ,26  ,11  ,32  ,11  ,19  ,26  ,4  as i32;
let mut  param2 : &[i32] = 16  ,14  ,23  ,41  ,7  ,28  ,12  ,38  ,23  ,2  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ] , param1 [ i ] , param2 [ i ]) ==  f_gold ( param0 [ i ] , param1 [ i ] , param2 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
