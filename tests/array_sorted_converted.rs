#![allow(warnings, unused)]
use std::*;
fn main() {
    let mut x: i32 = 4 as i32;
    let mut // Handling Pointers...
    y: *mut i32 = &x as i32;
    (*y) += 1;
    println!("{}", *y);
    return 0;
}
