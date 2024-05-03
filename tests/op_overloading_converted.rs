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
#[derive(Default)]
pub struct Complex {
    real: i32,
    imag: i32,
}
impl Complex {
    pub fn new(mut r: i32, mut i: i32) -> Complex {
        real = r as i32;
        imag = i;

        /*
            This is a constructor method.
            Please appropriate members to the struct constructor as per your logic.
            Currently the constructor returns a struct with all the defaults for the data types in the struct.
        */
        Complex {
            ..Default::default()
        }
    }
}
impl Add<&Complex> for Complex {
    type Output = Self;
    fn add(self, obj: &mut Complex) -> Self::Output {
        let mut res = Complex::new(0, 0);
        res.real = self.real + obj.real;
        res.imag = self.imag + obj.imag;
        return res;
    }
}
impl Complex {
    pub fn print(&mut self) {
        print!("{} + i{}{}", self.real, self.imag, '\n');
    }
}
fn main() {
    let mut c1 = Complex::new(10, 5);
    let mut c2 = Complex::new(2, 4);
    let mut c3: Complex = c1 + c2;
    c3.print();
}
