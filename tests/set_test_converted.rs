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
    let mut mySet = set::new().clone();
    let mut vecSet = set::new().clone();
    let mut v1 = vector![1, 2, 3].clone();
    vecSet.insert(v1);
    if mySet.empty() {
        print!("Set is empty\n");
    } else {
        print!("Set is not empty\n");
    }
    mySet.insert(5);
    mySet.insert(10);
    mySet.insert(15);
    mySet.insert(20);
    print!("Size of set: {}\n", mySet.size());
    print!("Count of 10 in set: {}\n", mySet.count(10));
    print!("Count of 25 in set: {}\n", mySet.count(25));
    mySet.erase(15);
    print!("Size of set after erasing: {}\n", mySet.size());
    let mut anotherSet = set::new().clone();
    anotherSet.insert(100);
    anotherSet.insert(200);
    mySet.swap(&mut anotherSet);
    print!("Size of mySet after swapping: {}\n", mySet.size());
    print!("Size of anotherSet after swapping: {}\n", anotherSet.size());
    mySet.clear();
    print!("Size of mySet after clearing: {}\n", mySet.size());
}
