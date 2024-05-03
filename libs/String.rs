use std::cmp::Ordering;
use std::fmt;
use std::ops::{Index, IndexMut};
#[derive(Clone, PartialEq, Eq, PartialOrd, Ord, Debug)]
pub struct string {
    pub string: std::string::String,
}

impl string {
    pub fn new() -> Self {
        string {
            string: std::string::String::new(),
        }
    }

    pub fn from_string(string: std::string::String) -> Self {
        string { string }
    }

    pub fn size(&self) -> usize {
        self.string.len()
    }

    pub fn length(&self) -> usize {
        self.string.chars().count()
    }

    pub fn resize(&mut self, new_len: usize, fill_char: char) {
        if new_len > self.size() {
            self.string
                .push_str(&fill_char.to_string().repeat(new_len - self.size()));
        } else {
            self.string.truncate(new_len);
        }
    }

    pub fn clear(&mut self) {
        self.string.clear();
    }

    pub fn empty(&self) -> bool {
        self.string.is_empty()
    }

    pub fn at(&self, index: usize) -> char {
        self.string.chars().nth(index).unwrap()
    }

    pub fn back(&self) -> char {
        self.string.chars().last().unwrap()
    }

    pub fn front(&self) -> char {
        self.string.chars().next().unwrap()
    }

    pub fn append(&mut self, other: string) {
        self.string.push_str(&other.string);
    }

    pub fn push_back(&mut self, ch: char) {
        self.string.push(ch);
    }

    pub fn assign(&mut self, count: usize, ch: char) {
        self.string = ch.to_string().repeat(count);
    }

    pub fn replace(&mut self, pos: usize, len: usize, other: string) {
        let mut new_string = std::string::String::new();
        new_string.push_str(&self.string[..pos]);
        new_string.push_str(&other.string);
        new_string.push_str(&self.string[pos + len..]);
        self.string = new_string;
    }

    pub fn swap(&mut self, other: &mut string) {
        std::mem::swap(&mut self.string, &mut other.string);
    }

    pub fn pop_back(&mut self) {
        self.string.pop();
    }

    pub fn substr(&self, pos: usize, len: usize) -> Self {
        string::from_string(self.string[pos..pos + len].to_string())
    }

    pub fn from(input: &str) -> Self {
        string {
            string: input.to_string(),
        }
    }
    // pub fn as_mut_vec(&mut self) -> &mut Vec<char> {
    //     self.string.as_mut_vec()
    // }
}

impl Index<usize> for string {
    type Output = char;

    fn index(&self, index: usize) -> &Self::Output {
        Box::leak(Box::new(self.string.chars().nth(index).unwrap()))
    }
}

// impl IndexMut<usize> for string {
//     fn index_mut(&mut self, index: usize) -> &mut Self::Output {
//         let len = self.string.len();
//         if index >= len {
//             self.resize(index + 1, '\0');
//         }
//         &mut self.string[index..].chars().next_mut().unwrap()
//     }
// }

impl std::ops::Add<string> for string {
    type Output = string;

    fn add(mut self, mut other: string) -> Self::Output {
        self.string.push_str(&other.string);
        self
    }
}

impl std::ops::AddAssign<string> for string {
    fn add_assign(&mut self, other: string) {
        self.string.push_str(&other.string);
    }
}

impl fmt::Display for string {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.string)
    }
}

#[macro_export]
macro_rules! string {
    ($($char:expr),*) => {
        {
            let mut temp_string = string::new();
            $(temp_string.push_back($char);)*
            temp_string
        }
    };
}
