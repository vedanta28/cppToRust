use std::ops::Index;
use std::vec::Vec;
use ListInit;

#[derive(Clone, PartialEq, Eq, PartialOrd, Ord, Debug)]
pub struct stack<T> {
    pub data: Vec<T>,
}

impl<T> stack<T> {
    pub fn new() -> Self {
        stack { data: Vec::new() }
    }

    pub fn assign(&mut self, count: usize, value: T)
    where
        T: Clone,
    {
        self.data = vec![value; count];
    }

    pub fn at(&self, index: usize) -> &T {
        self.data.get(index).unwrap()
    }

    pub fn empty(&self) -> bool {
        self.data.is_empty()
    }

    pub fn size(&self) -> usize {
        self.data.len()
    }

    pub fn top(&self) -> &T {
        self.data.last().unwrap()
    }

    pub fn push(&mut self, item: T) {
        self.data.push(item)
    }

    pub fn emplace(&mut self, item: T) {
        self.data.push(item);
    }

    pub fn pop(&mut self) -> T {
        self.data.pop().unwrap()
    }

    pub fn clear(&mut self) {
        self.data.clear();
    }

    pub fn resize(&mut self, new_size: usize, value: T)
    where
        T: Clone,
    {
        self.data.resize(new_size, value);
    }

    pub fn swap(&mut self, other: &mut stack<T>) {
        std::mem::swap(&mut self.data, &mut other.data);
    }
}

impl<T> ListInit<T> for stack<T> {
    fn init_list(elements: Vec<T>) -> Self {
        stack { data: elements }
    }
}

// List initialization macro
#[macro_export]
macro_rules! stack {
    ($($elem:expr),*) => {
        {
            let elements = vec![$($elem),*];
            <vector<_> as ListInit<_>>::init_list(elements)
        }
    };
}

// Index trait implementation
impl<T> Index<usize> for stack<T> {
    type Output = T;

    fn index(&self, index: usize) -> &T {
        &self.data[index]
    }
}
