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
fn  f_gold  ( mut  start :i32 , mut  end :i32 , mut  arr  [  ] :i32 )  -> i32{ 
let mut  frequency : // Templates are yet to supported! Currently copying them as it is!
 unordered_map<int,int> ;
let mut  i :i32 =  start  as i32;
while  i  <=  end {
 frequency [ arr [ i ]]+=1 ;
 i +=1 ;}
let mut  count :i32 = 0  as i32;
// Will deal with for Range Declarations and Initializers later
for   x  in  frequency  if  x . first  ==  x . second {
 count +=1 ;
}
 return  count ;
} 
fn  f_filled  ( mut  start :i32 , mut  end :i32 , mut  arr  [  ] :i32 )  -> i32{ 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0 : &[i32] = 0  ,1  ,3  ,10  ,2  ,0  ,14  ,29  ,31  ,21  as i32;
let mut  param1 : &[i32] = 31  ,25  ,4  ,15  ,3  ,6  ,18  ,33  ,19  ,32  as i32;
let mut  param2_0 : &[i32] = 1  ,2  ,2  ,3  ,3  ,3  ,12  ,13  ,18  ,18  ,26  ,28  ,29  ,36  ,37  ,39  ,40  ,49  ,55  ,57  ,63  ,69  ,69  ,73  ,85  ,86  ,87  ,87  ,89  ,89  ,90  ,91  ,92  ,93  ,93  ,93  ,95  ,99  as i32;
let mut  param2_1 : &[i32] = 24  ,- 62  ,2  ,1  ,94  ,56  ,- 22  ,- 70  ,- 22  ,- 34  ,- 92  ,- 18  ,56  ,2  ,60  ,38  ,- 88  ,16  ,- 28  ,30  ,- 30  ,58  ,- 80  ,94  ,6  ,56  as i32;
let mut  param2_2 : &[i32] = 0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  as i32;
let mut  param2_3 : &[i32] = 84  ,13  ,81  ,40  ,87  ,82  ,50  ,30  ,90  ,80  ,81  ,70  ,14  ,54  ,72  ,93  ,78  ,27  ,61  as i32;
let mut  param2_4 : &[i32] = - 20  ,20  ,34  ,60  ,90  as i32;
let mut  param2_5 : &[i32] = 1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  as i32;
let mut  param2_6 : &[i32] = 11  ,18  ,18  ,19  ,25  ,30  ,42  ,42  ,56  ,58  ,63  ,66  ,67  ,68  ,69  ,75  ,78  ,83  ,83  as i32;
let mut  param2_7 : &[i32] = - 24  ,- 82  ,24  ,- 84  ,94  ,2  ,- 30  ,86  ,58  ,- 56  ,- 96  ,60  ,- 38  ,76  ,94  ,74  ,- 98  ,- 84  ,- 38  ,46  ,4  ,- 84  ,- 90  ,- 28  ,- 50  ,46  ,16  ,28  ,- 14  ,- 82  ,- 64  ,42  ,64  ,- 2  ,- 40  ,96  ,60  ,2  ,- 86  ,32  ,38  ,- 66  as i32;
let mut  param2_8 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  as i32;
let mut  param2_9 : &[i32] = 2  ,91  ,42  ,85  ,97  ,92  ,24  ,39  ,63  ,89  ,31  ,59  ,51  ,89  ,72  ,62  ,26  ,92  ,75  ,4  ,6  ,13  ,20  ,95  ,22  ,30  ,52  ,60  ,37  ,27  ,49  ,15  ,67  ,26  as i32;
let mut // Handling Pointers...
*mut  param2 : [ i32;10 ] =  param2_0  , param2_1  , param2_2  , param2_3  , param2_4  , param2_5  , param2_6  , param2_7  , param2_8  , param2_9  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 if  f_filled ( param0 [ i ] , param1 [ i ] , param2 [ i ]) ==  f_gold ( param0 [ i ] , param1 [ i ] , param2 [ i ]){ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
