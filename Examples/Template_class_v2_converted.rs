#![allow(warnings, unused)]
// Templates are not yet supported for conversion
i32#[derive(Default)]
pub  struct  Array < T >  {
 ptr :*muti32 T ,
 size :i32,
 }
// Templates are not yet supported for conversion
impl< T >  Array<T>{
fn  Array < T >  ( mut  arr  [  ] :i32 T  , mut  s :i32 )  -> i32// Templates are yet to supported! Currently copying them as it is!
 Array<T> { 
 ptr  =  T  s ;
 size  =  s ;
let mut  i :i32 = 0 ;
while  i  <  size {
 ptr  [  i  ]  =  arr [ i ];
 i +=1 ;}
} 
}
// Templates are not yet supported for conversion
impl< T >  Array<T>{
fn  print < T >  (  ) i32{ 
let mut  i :i32 = 0 ;
while  i  <  size {
 std::  println! (" {}",*(ptr+i));
 i +=1 ;}
} 
}
