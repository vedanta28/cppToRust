// Templates are not yet supported for conversion
#[derive(Default)]
pub  struct  Array < T >  {
 ptr :*mut T ,
 size : i32 ,
 Array  ( mut  arr  [  ] : T  , mut  s : i32  ) ,
 print  (  ) :,
 }
// Templates are not yet supported for conversion
fn // Nested name Specifiers are yet to supported! Currently copying them as it is!
 ::  Array < T > < T >  ( mut  arr  [  ] : T  , mut  s : i32  )  -> // Templates are yet to supported! Currently copying them as it is!
 Array<T> { 
 ptr  =  T  s ;
 size  =  s ;
let mut  i : i32  = 0;
while  i  <  size {
 ptr  [  i  ]  =  arr [ i ];
 i +=1 ;}
} 
// Templates are not yet supported for conversion
fn // Nested name Specifiers are yet to supported! Currently copying them as it is!
 Array<T>::  print < T >  (  ) { 
let mut  i : i32  = 0;
while  i  <  size {
// Nested name Specifiers are yet to supported! Currently copying them as it is!
 std::  println! (" {}",*(ptr+i));
 i +=1 ;}
} 
