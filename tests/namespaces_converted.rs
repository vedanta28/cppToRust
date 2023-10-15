#![allow(warnings, unused)]
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
    use myapp::xd::*;
    myapp::xd::tr();
}
