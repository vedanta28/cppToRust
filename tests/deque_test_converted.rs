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
    let mut deque1 = deque::new().clone();
    deque1.push_back(1);
    deque1.push_back(2);
    deque1.push_back(3);
    print!("Deque 1: ");
    let mut i: usize = 0 as usize;
    while i < deque1.size() {
        print!("{} ", deque1[i as usize]);
        i += 1;
    }
    print!("\n");
    let mut deque2 = deque![6, 7, 8, 9, 10].clone();
    deque2.push_back(4);
    deque2.push_back(5);
    print!("Deque 2: ");
    let mut i: usize = 0 as usize;
    while i < deque2.size() {
        print!("{} ", deque2[i as usize]);
        i += 1;
    }
    print!("\n");
    deque1.swap(&mut deque2);
    print!("Deque 1 (after swap): ");
    let mut i: usize = 0 as usize;
    while i < deque1.size() {
        print!("{} ", deque1[i as usize]);
        i += 1;
    }
    print!("\n");
    print!("Deque 2 (after swap): ");
    let mut i: usize = 0 as usize;
    while i < deque2.size() {
        print!("{} ", deque2[i as usize]);
        i += 1;
    }
    print!("\n");
    print!("Element at index 1 in deque 1: {}\n", deque1[1 as usize]);
    print!("Front element of deque 1: {}\n", deque1.front());
    print!("Back element of deque 1: {}\n", deque1.back());
    if deque1.empty() {
        print!(" The deque is empty \n");
    } else {
        print!(" The deque is not empty() \n");
    }
    print!("Size of deque 1: {}\n", deque1.size());
    deque1.clear();
    print!("Deque 1 (after clear): ");
    let mut i: usize = 0 as usize;
    while i < deque1.size() {
        print!("{} ", deque1[i as usize]);
        i += 1;
    }
    print!("\n");
    deque1.push_front(10);
    deque1.push_front(20);
    deque1.push_front(30);
    print!("Deque 1 (after push_front): ");
    let mut i: usize = 0 as usize;
    while i < deque1.size() {
        print!("{} ", deque1[i as usize]);
        i += 1;
    }
    print!("\n");
    deque1.pop_front();
    print!("Deque 1 (after pop_front): ");
    let mut i: usize = 0 as usize;
    while i < deque1.size() {
        print!("{} ", deque1[i as usize]);
        i += 1;
    }
    print!("\n");
    deque1.resize(5, 99);
    print!("Deque 1 (after resize): ");
    let mut i: usize = 0 as usize;
    while i < deque1.size() {
        print!("{} ", deque1[i as usize]);
        i += 1;
    }
    print!("\n");
    deque1.emplace_front(50);
    print!("Deque 1 (after emplace_front): ");
    let mut i: usize = 0 as usize;
    while i < deque1.size() {
        print!("{} ", deque1[i as usize]);
        i += 1;
    }
    deque1 = deque2.clone();
    print!("\n");
    print!("Deque 1 (after assignment): ");
    let mut i: usize = 0 as usize;
    while i < deque1.size() {
        print!("{} ", deque1[i as usize]);
        i += 1;
    }
}
