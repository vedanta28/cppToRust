use std::io;
mod myapp {
    pub fn error() { /* ... */ }
    pub const SOME_VALUE :i32 = 20;
    pub fn doSomething(value: i32) { println!("{}", value); }
}

fn main() {
    println!("{}", myapp::SOME_VALUE);
    myapp::error();
    myapp::doSomething(5);

    use myapp::*;

    error();
    println!("{}", SOME_VALUE);
}