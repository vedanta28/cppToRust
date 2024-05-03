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
    let mut v1 = vector::new().clone();
    v1.push_back(10);
    v1.emplace_back(20);
    let mut i: usize = 0 as usize;
    while i < v1.size() {
        print!("{} ", v1[i as usize]);
        i += 1;
    }
    print!("\n");
    v1.pop_back();
    let mut i: usize = 0 as usize;
    while i < v1.size() {
        print!("{} ", v1[i as usize]);
        i += 1;
    }
    print!("\n");
    let mut v2 = vector![1, 2, 3].clone();
    let mut i: usize = 0 as usize;
    while i < v2.size() {
        print!("{} ", v2[i as usize]);
        i += 1;
    }
    print!("\n");
    v2 = v1.clone();
    let mut i: usize = 0 as usize;
    while i < v2.size() {
        print!("{} ", v2[i as usize]);
        i += 1;
    }
    print!("\n");
    v2.assign(3, 3);
    let mut i: usize = 0 as usize;
    while i < v2.size() {
        print!("{} ", v2[i as usize]);
        i += 1;
    }
    print!("\n");
    v2.resize(2, 0);
    let mut i: usize = 0 as usize;
    while i < v2.size() {
        print!("{} ", v2[i as usize]);
        i += 1;
    }
    print!("\n");
    v2.resize(4, 5);
    let mut i: usize = 0 as usize;
    while i < v2.size() {
        print!("{} ", v2[i as usize]);
        i += 1;
    }
    print!("\n");
    print!(
        "{} {} {} {} {}\n",
        v2[1 as usize],
        v2.at(1),
        v2.size(),
        v2.front(),
        v2.back()
    );
    v2.clear();
    if v2.empty() {
        print!("Vector is Empty\n");
    } else {
        print!("Vector is Non-Empty\n");
    }
    v2 = vector![1, 2].clone();
    let mut i: usize = 0 as usize;
    while i < v1.size() {
        print!("{} ", v1[i as usize]);
        i += 1;
    }
    print!("\n");
    let mut i: usize = 0 as usize;
    while i < v2.size() {
        print!("{} ", v2[i as usize]);
        i += 1;
    }
    print!("\n");
    v1.swap(&mut v2);
    let mut i: usize = 0 as usize;
    while i < v1.size() {
        print!("{} ", v1[i as usize]);
        i += 1;
    }
    print!("\n");
    let mut i: usize = 0 as usize;
    while i < v2.size() {
        print!("{} ", v2[i as usize]);
        i += 1;
    }
    print!("\n");
}
