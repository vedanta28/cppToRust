#![allow(warnings, unused)]
// Templates are not yet fully supported for conversion
 #[derive(Default)]
pub  struct  Array < T >  {
 ptr :*mut   T ,
 size :i32,
 }
impl < T >  Array < T >  {
pub fn  new  ( mut  arr  [  ] :  T  , mut  s :i32 )  -> Array< T >  { 
 ptr  =  T  s  as i32;
 size  =  s ;
let mut  i :i32 = 0  as i32;
while  i  <  size {
 ptr  [  i  ]  =  arr [ i ];
 i +=1 ;}

/*
	This is a constructor method.
	Please appropriate members to the struct constructor as per your logic.
	Currently the constructor returns a struct with all the defaults for the data types in the struct.
*/
Array{..Default::default()}
}
pub fn  print  ( &mut self )  { 
let mut  i :i32 = 0  as i32;
while  i  <  self.size {
 std::  println! (" {}",*(ptr+i));
 i +=1 ;}
} 
 }
