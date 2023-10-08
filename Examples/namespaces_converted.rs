// Using Namespace directives are not yet supported in this transpiler... Copying as it is
use std::*;
// Variables in namespaces are partically supported....
mod myapp {
    // Variables in namespaces are partically supported....
    pub mod xd {
        // Variables in namespaces are partically supported....
        pub mod tl {}
        pub fn tr() {
            println!("Inside");
        }
    }
    pub fn pr() {
        println!("Hello");
    }
}
fn main() {
    myapp::pr();
    // Using Namespace directives are not yet supported in this transpiler... Copying as it is
    use myapp::xd::*;
    myapp::xd::tr();
}
