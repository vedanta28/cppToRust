use std::collections::VecDeque;
use std::ops::Index;

#[derive(Clone, PartialEq, Eq, PartialOrd, Ord, Debug)]
pub struct deque<T> {
    pub deque: VecDeque<T>,
}

impl<T: Clone> deque<T> {
    // Constructor
    pub fn new() -> Self {
        deque {
            deque: VecDeque::new(),
        }
    }

    //push defaults to push_back
    pub fn push(&mut self, value: T) {
        self.push_back(value);
    }

    //pop defaults to pop_front
    pub fn pop(&mut self) -> Option<T> {
        self.pop_front()
    }

    // Operator=
    pub fn assign(&mut self, other: deque<T>) {
        self.deque = other.deque;
    }

    // At()
    pub fn at(&self, index: usize) -> Option<&T> {
        self.deque.get(index)
    }

    // Operator[]
    pub fn index(&self, index: usize) -> Option<&T> {
        self.at(index)
    }

    // Front()
    pub fn front(&self) -> &T {
        self.deque.front().unwrap()
    }

    // Back()
    pub fn back(&self) -> &T {
        self.deque.back().unwrap()
    }

    // Empty()
    pub fn empty(&self) -> bool {
        self.deque.is_empty()
    }

    // Size()
    pub fn size(&self) -> usize {
        self.deque.len()
    }

    // Clear()
    pub fn clear(&mut self) {
        self.deque.clear();
    }

    // PushBack()
    pub fn push_back(&mut self, value: T) {
        self.deque.push_back(value);
    }

    // PopBack()
    pub fn pop_back(&mut self) -> Option<T> {
        self.deque.pop_back()
    }

    // PushFront()
    pub fn push_front(&mut self, value: T) {
        self.deque.push_front(value);
    }

    // PopFront()
    pub fn pop_front(&mut self) -> Option<T> {
        self.deque.pop_front()
    }

    // EmplaceFront()
    pub fn emplace_front(&mut self, value: T) {
        self.deque.push_front(value);
    }

    // Resize()
    pub fn resize(&mut self, new_size: usize, value: T) {
        if new_size > self.deque.len() {
            self.deque.resize_with(new_size, || value.clone());
        } else {
            self.deque.truncate(new_size);
        }
    }

    // Swap()
    pub fn swap(&mut self, other: &mut deque<T>) {
        std::mem::swap(&mut self.deque, &mut other.deque);
    }
}
impl<T> Index<usize> for deque<T> {
    type Output = T;

    fn index(&self, index: usize) -> &Self::Output {
        // Panic if the index is out of bounds
        &self.deque[index]
    }
}

#[macro_export]
macro_rules! deque {
    () => {
        deque::new()
    };
    ($($item:expr),+ $(,)?) => {
        {
            let mut temp_deque = deque::new();
            $(temp_deque.push_back($item);)*
            temp_deque
        }
    };
}
