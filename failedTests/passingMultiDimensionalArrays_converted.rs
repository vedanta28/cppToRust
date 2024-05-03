#![allow(warnings, unused)]
use std::ops::{Add, AddAssign, BitAnd, BitAndAssign, BitOr, BitOrAssign};
use std::ops::{BitXor, BitXorAssign, Div, DivAssign, Index, Mul, MulAssign};
use std::ops::{Neg, Not, Rem, RemAssign, Shl, ShlAssign, Shr, ShrAssign, Sub, SubAssign};
#[path = "../libs/Vector.rs"]
pub mod Vector;
use Vector::{vector, ListInit};

#[path = "../libs/Stack.rs"]
pub mod Stack;
use Stack::stack;

#[path = "../libs/Map.rs"]
pub mod Map;
use Map::map;
#[path = "../libs/Unordered_map.rs"]
pub mod Unordered_map;
use Unordered_map::unordered_map;

#[path = "../libs/Deque.rs"]
pub mod Deque;
use Deque::deque;

#[path = "../libs/Set.rs"]
pub mod Set;
use Set::set;

#[path = "../libs/UnorderedSet.rs"]
pub mod UnorderedSet;
use UnorderedSet::unordered_set;

#[path = "../libs/String.rs"]
pub mod String;
use String::string;
fn transpose(mut a: [[i32; 3]; 3], mut n: usize) {
    let mut i: usize = 0 as usize;
    while i < n {
        let mut j: usize = i as usize;
        while j < n {
            let mut temp: i32 = a[i as usize][j as usize];
            a[i as usize][j as usize] = a[j as usize][i as usize];
            a[j as usize][i as usize] = temp;
            j += 1;
        }
        i += 1;
    }
}
fn print(mut a: [[i32; 3]; 3], mut n: usize) {
    let mut i: usize = 0 as usize;
    while i < n {
        let mut j: usize = 0 as usize;
        while j < n {
            print!("{} ", a[i as usize][j as usize]);
            j += 1;
        }
        print!("\n");
        i += 1;
    }
}
fn main() {
    let mut a: [[i32; 3]; 3] = [(1, 2, 3), (4, 5, 6), (7, 8, 9)];
    transpose(a, 3);
    print(a, 3);
}
