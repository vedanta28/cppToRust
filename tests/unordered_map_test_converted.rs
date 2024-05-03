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
use std::*;
use String::string;
fn main() {
    let mut mp = unordered_map::new();
    let mut vecmp = unordered_map::new();
    let mut v = vector![string::from("a")].clone();
    vecmp.insert((1, v));
    if mp.empty() {
        print!("Set is empty\n");
    } else {
        print!("Set is not empty\n");
    }
    mp.insert((1, 1));
    mp.insert((2, 2));
    print!("Size of mp:{}\n", mp.size());
    print!("Count of 1 in mp:{}\n", mp.count(1));
    print!("Count of 3 in mp:{}\n", mp.count(3));
    mp.erase(1);
    print!("Size of mp after removing:{}\n", mp.size());
    let mut mp2 = unordered_map::new();
    mp2.insert((3, 3));
    mp2.insert((5, 5));
    mp.swap(&mut mp2);
    print!("Size of mp after swapping:{}\n", mp.size());
    print!("Size of mp2 after swapping:{}\n", mp2.size());
    mp.clear();
    print!("size of mp after clear{}\n", mp.size());
}
