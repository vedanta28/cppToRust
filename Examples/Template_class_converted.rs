// Templates are not yet supported for conversion
#[derive(Default)]
pub  struct  Array < T >  {
 ptr :*mut T ,
 size : i32 ,
 }
impl < T >  Array < T >  {
pub fn  new  ( mut  arr  [  ] : T  , mut  s : i32  )  -> Array { 
 ptr  =  T  s ;
 self.size  =  s ;
let mut  i : i32  = 0;
while  i  <  self.size {
 ptr  [  i  ]  =  arr [ i ];
 i +=1 ;}

/*
	This is a constructor method.
	Please appropriate members to the struct constructor as per your logic.
	Currently the constructor returns a struct with all the defaults for the data types in the struct.
*/
Array{..Default::default()}
}
pub fn  print  ( &mut self ) { 
let mut  i : i32  = 0;
while  i  <  self.size {
// Nested name Specifiers are yet to supported! Currently copying them as it is!
 std::  println! (" {}",*(ptr+i));
 i +=1 ;}
} 
 }
