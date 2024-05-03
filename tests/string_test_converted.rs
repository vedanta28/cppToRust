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
    let mut s = string::from("Hello, World!").clone();
    print!("Original string: {}\n", s);
    print!("Size of string: {}\n", s.size());
    print!("Length of string: {}\n", s.length());
    s.resize(7, '0');
    print!("Resized string: {}\n", s);
    s.clear();
    print!("Cleared string: {}\n", s);
    if s.empty() {
        print!("String is empty\n");
    } else {
        print!("String is not empty\n");
    }
    s = string::from("New Value").clone();
    print!("New value assigned: {}\n", s);
    print!("Character at index 2: {}\n", s[2 as usize]);
    print!("Character at index 4: {}\n", s.at(4));
    print!("First character: {}\n", s.front());
    print!("Last character: {}\n", s.back());
    s += string::from(" appended");
    print!("String after operator+=: {}\n", s);
    s.append(string::from(" with append"));
    print!("String after append: {}\n", s);
    s.push_back('!');
    print!("String after push_back: {}\n", s);
    s.assign(5, 'A');
    print!("String after assign: {}\n", s);
    s.replace(2, 3, string::from("XYZ"));
    print!("String after replace: {}\n", s);
    let mut anotherString = string::from("Another string").clone();
    print!("Before swap: {}, {}\n", s, anotherString);
    s.swap(&mut anotherString);
    print!("After swap: {}, {}\n", s, anotherString);
    s.pop_back();
    print!("String after pop_back: {}\n", s);
    let mut substr = s.substr(2, 4).clone();
    print!("Substring: {}\n", substr);
}
