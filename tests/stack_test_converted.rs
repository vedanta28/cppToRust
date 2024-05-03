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
    let mut s1 = stack::new().clone();
    if s1.empty() {
        print!("Stack is Empty\n");
    } else {
        print!("Stack is Non-Empty\n");
    }
    s1.push(10);
    s1.push(20);
    s1.emplace(20);
    print!("S1.size() = {}\n", s1.size());
    while !s1.empty() {
        print!("{} ", s1.top());
        s1.pop();
    }
    print!("\n");
    let mut s2 = stack::new().clone();
    s2 = s1.clone();
    s1.push(4);
    print!("Before swap\n");
    print!(" s1.len() = {}\n", s1.size());
    print!(" s2.len() = {}\n", s2.size());
    s1.swap(&mut s2);
    print!("After swap\n");
    print!(" s1.len() = {}\n", s1.size());
    print!(" s2.len() = {}\n", s2.size());
}
