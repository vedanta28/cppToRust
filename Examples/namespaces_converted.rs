// Using Namespace directives are not yet supported in this transpiler... Copying as it is
// using namespace std ;
 mod  myapp {
let mut  x : i32  = 5;
pub mod  xd {
pub mod  tl {
}
pub fn  tr  (  ) { 
 println! ("Inside");
} 
}
pub fn  pr  (  ) { 
 println! ("Hello");
} 
}
fn  main  (  ) { 
 myapp // Nested name Specifiers are yet to supported! Currently copying them as it is!
 ::  pr  (  ) ;
// Nested name Specifiers are yet to supported! Currently copying them as it is!
 myapp::  xd // Nested name Specifiers are yet to supported! Currently copying them as it is!
 ::  tr  (  ) ;
} 
