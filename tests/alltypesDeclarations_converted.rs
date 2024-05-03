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
fn main() {
    const a: i32 = 5 as i32;
    let mut b = 4 * 2 + 1;
    let mut c: char = 'a' as char;
    let mut d: char;
    let mut d: bool = true as bool;
    let mut e: i64 = 1 as i64;
    let mut e: u64 = if d { 5 } else { 6 } as u64;
    print!("{}", e);
}
