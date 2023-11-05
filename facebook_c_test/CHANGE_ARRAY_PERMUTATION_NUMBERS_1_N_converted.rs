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
fn  f_gold  ( mut  a  [  ] :i32 , mut  n :i32 )  { 
let mut  count : // Templates are yet to supported! Currently copying them as it is!
 unordered_map<int,int> ;
let mut  i :i32 = 0  as i32;
while  i  <  n {
 count [ a [ i ]]+=1 ;
 i +=1 ;}
let mut  next_missing :i32 = 1  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  n {
 if  count [ a [ i ]] != 1  ||  a [ i ] >  n  ||  a [ i ] < 1 { 
 count [ a [ i ]]-=1 ;
 while  count . find ( next_missing ) !=  count . end (){
 next_missing +=1 ;
}
 a  =  next_missing ;
 count  = 1 ;
} 
 i +=1 ;}
} 
fn  f_filled  ( mut  a  [  ] :i32 , mut  n :i32 )  { 
} 
fn  main  (   ) { 
let mut  n_success :i32 = 0  as i32;
let mut  param0_0 : &[i32] = 19  as i32;
let mut  param0_1 : &[i32] = - 47  ,72  as i32;
let mut  param0_2 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  as i32;
let mut  param0_3 : &[i32] = 93  ,3  ,20  ,59  ,36  ,19  ,90  ,67  ,19  ,20  ,96  ,71  ,52  ,33  ,40  ,39  as i32;
let mut  param0_4 : &[i32] = - 98  ,- 93  ,- 91  ,- 89  ,- 63  ,- 58  ,- 52  ,- 52  ,- 46  ,- 40  ,- 25  ,- 16  ,- 10  ,- 1  ,- 1  ,4  ,12  ,12  ,13  ,13  ,16  ,20  ,29  ,29  ,31  ,40  ,44  ,47  ,48  ,51  ,52  ,52  ,59  ,60  ,61  ,64  ,66  ,78  ,85  ,97  as i32;
let mut  param0_5 : &[i32] = 0  ,1  ,1  ,1  ,1  ,1  ,1  ,0  ,1  ,0  ,0  ,1  ,0  ,1  ,0  ,1  ,0  ,1  ,1  ,1  ,1  ,1  ,0  ,0  ,0  as i32;
let mut  param0_6 : &[i32] = 4  ,6  ,8  ,17  ,19  ,21  ,22  ,24  ,27  ,27  ,28  ,30  ,30  ,30  ,32  ,33  ,35  ,37  ,38  ,44  ,46  ,46  ,48  ,49  ,51  ,53  ,54  ,59  ,60  ,61  ,63  ,64  ,64  ,69  ,76  ,85  ,86  ,87  ,92  ,93  ,93  ,95  ,97  ,97  ,97  ,98  ,99  ,99  as i32;
let mut  param0_7 : &[i32] = - 75  ,- 46  ,- 42  ,- 33  ,4  ,74  ,- 76  ,14  ,- 68  ,75  ,- 14  ,51  ,94  ,27  ,55  ,30  ,- 83  ,4  as i32;
let mut  param0_8 : &[i32] = 0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  as i32;
let mut  param0_9 : &[i32] = 24  ,13  ,60  ,7  ,57  ,36  ,45  ,20  ,65  ,8  ,16  ,14  ,76  ,87  ,15  ,92  ,98  ,66  ,32  ,87  ,63  ,86  ,51  ,25  ,58  as i32;
let mut // Handling Pointers...
*mut  param0 : [ i32;10 ] =  param0_0  , param0_1  , param0_2  , param0_3  , param0_4  , param0_5  , param0_6  , param0_7  , param0_8  , param0_9  as i32;
let mut  param1 : &[i32] = 0  ,1  ,18  ,9  ,22  ,12  ,26  ,9  ,5  ,24  as i32;
let mut  filled_function_param0_0 : &[i32] = 19  as i32;
let mut  filled_function_param0_1 : &[i32] = - 47  ,72  as i32;
let mut  filled_function_param0_2 : &[i32] = 0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  as i32;
let mut  filled_function_param0_3 : &[i32] = 93  ,3  ,20  ,59  ,36  ,19  ,90  ,67  ,19  ,20  ,96  ,71  ,52  ,33  ,40  ,39  as i32;
let mut  filled_function_param0_4 : &[i32] = - 98  ,- 93  ,- 91  ,- 89  ,- 63  ,- 58  ,- 52  ,- 52  ,- 46  ,- 40  ,- 25  ,- 16  ,- 10  ,- 1  ,- 1  ,4  ,12  ,12  ,13  ,13  ,16  ,20  ,29  ,29  ,31  ,40  ,44  ,47  ,48  ,51  ,52  ,52  ,59  ,60  ,61  ,64  ,66  ,78  ,85  ,97  as i32;
let mut  filled_function_param0_5 : &[i32] = 0  ,1  ,1  ,1  ,1  ,1  ,1  ,0  ,1  ,0  ,0  ,1  ,0  ,1  ,0  ,1  ,0  ,1  ,1  ,1  ,1  ,1  ,0  ,0  ,0  as i32;
let mut  filled_function_param0_6 : &[i32] = 4  ,6  ,8  ,17  ,19  ,21  ,22  ,24  ,27  ,27  ,28  ,30  ,30  ,30  ,32  ,33  ,35  ,37  ,38  ,44  ,46  ,46  ,48  ,49  ,51  ,53  ,54  ,59  ,60  ,61  ,63  ,64  ,64  ,69  ,76  ,85  ,86  ,87  ,92  ,93  ,93  ,95  ,97  ,97  ,97  ,98  ,99  ,99  as i32;
let mut  filled_function_param0_7 : &[i32] = - 75  ,- 46  ,- 42  ,- 33  ,4  ,74  ,- 76  ,14  ,- 68  ,75  ,- 14  ,51  ,94  ,27  ,55  ,30  ,- 83  ,4  as i32;
let mut  filled_function_param0_8 : &[i32] = 0  ,0  ,0  ,0  ,0  ,1  ,1  ,1  ,1  as i32;
let mut  filled_function_param0_9 : &[i32] = 24  ,13  ,60  ,7  ,57  ,36  ,45  ,20  ,65  ,8  ,16  ,14  ,76  ,87  ,15  ,92  ,98  ,66  ,32  ,87  ,63  ,86  ,51  ,25  ,58  as i32;
let mut // Handling Pointers...
*mut  filled_function_param0 : [ i32;10 ] =  filled_function_param0_0  , filled_function_param0_1  , filled_function_param0_2  , filled_function_param0_3  , filled_function_param0_4  , filled_function_param0_5  , filled_function_param0_6  , filled_function_param0_7  , filled_function_param0_8  , filled_function_param0_9  as i32;
let mut  filled_function_param1 : &[i32] = 0  ,1  ,18  ,9  ,22  ,12  ,26  ,9  ,5  ,24  as i32;
let mut  i :i32 = 0  as i32;
while  i  <  len ( param0 ){
 f_filled  ( mut  i :  filled_function_param0  , mut  i :  filled_function_param1  ) ;
 f_gold  ( mut  i :  param0  , mut  i :  param1  ) ;
 if  equal ( begin ( param0 [ i ]) , end ( param0 [ i ]) , begin ( filled_function_param0 [ i ])) &&  param1 [ i ] ==  filled_function_param1 [ i ]{ 
 n_success  += 1 ;
} 
 i += 1;}
 println! ( "#Results:"  ," "  , n_success  ,", "  , len ( param0 ) );
 return 0 ;
} 
