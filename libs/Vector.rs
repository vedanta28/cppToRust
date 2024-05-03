use std::cmp::Ordering;
use std::ops::Index;
use std::vec::Vec;

#[derive(Clone, PartialEq, Eq, PartialOrd, Ord, Debug)]
pub struct vector<T> {
    pub data: Vec<T>,
}

impl<T> vector<T> {
    pub fn new() -> Self {
        vector { data: Vec::new() }
    }

    // assign
    pub fn assign(&mut self, count: usize, value: T)
    where
        T: Clone,
    {
        self.data = vec![value; count];
    }

    // at
    pub fn at(&self, index: usize) -> &T {
        self.data.get(index).unwrap()
    }

    // front
    pub fn front(&self) -> &T {
        self.data.first().unwrap()
    }

    // back
    pub fn back(&self) -> &T {
        self.data.last().unwrap()
    }

    // empty
    pub fn empty(&self) -> bool {
        self.data.is_empty()
    }

    // size
    pub fn size(&self) -> usize {
        self.data.len()
    }

    // clear
    pub fn clear(&mut self) {
        self.data.clear();
    }

    // insert
    pub fn insert(&mut self, index: usize, element: T) {
        self.data.insert(index, element);
    }

    // emplace
    pub fn emplace(&mut self, index: usize, element: T) {
        self.data.insert(index, element);
    }

    // push_back
    pub fn push_back(&mut self, element: T) {
        self.data.push(element);
    }

    // emplace_back
    pub fn emplace_back(&mut self, element: T) {
        self.data.push(element);
    }

    // pop_back
    pub fn pop_back(&mut self) -> Option<T> {
        self.data.pop()
    }

    // resize
    pub fn resize(&mut self, new_size: usize, value: T)
    where
        T: Clone,
    {
        self.data.resize(new_size, value);
    }

    // swap
    pub fn swap(&mut self, other: &mut vector<T>) {
        std::mem::swap(&mut self.data, &mut other.data);
    }
}

// Trait for list initialization
pub trait ListInit<T> {
    fn init_list(elements: Vec<T>) -> Self;
}

impl<T> ListInit<T> for vector<T> {
    fn init_list(elements: Vec<T>) -> Self {
        vector { data: elements }
    }
}

// List initialization macro
#[macro_export]
macro_rules! vector {
    ($($elem:expr),*) => {
        {
            let elements = vec![$($elem),*];
            <vector<_> as ListInit<_>>::init_list(elements)
        }
    };
}

// Index trait implementation
impl<T> Index<usize> for vector<T> {
    type Output = T;

    fn index(&self, index: usize) -> &T {
        &self.data[index]
    }
}
