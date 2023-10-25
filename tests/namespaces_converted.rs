#![allow(warnings, unused)]
// Variables in namespaces are partially supported....
mod myapp {
    // Variables in namespaces are partially supported....
    pub mod xd {
        // Variables in namespaces are partially supported....
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
    use myapp::xd::*;
    myapp::xd::tr();
}
