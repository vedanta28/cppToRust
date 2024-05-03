use std::collections::HashSet;
use std::hash::Hash;

#[derive(Clone, Debug)]
pub struct unordered_set<T> {
    set: HashSet<T>,
}

impl<T: Eq + Hash> unordered_set<T> {
    pub fn new() -> Self {
        unordered_set {
            set: HashSet::new(),
        }
    }

    pub fn empty(&self) -> bool {
        self.set.is_empty()
    }

    pub fn size(&self) -> usize {
        self.set.len()
    }

    pub fn clear(&mut self) {
        self.set.clear();
    }

    pub fn insert(&mut self, value: T) -> bool {
        self.set.insert(value)
    }

    pub fn erase(&mut self, value: T) -> bool {
        self.set.remove(&value)
    }

    pub fn swap(&mut self, other: &mut unordered_set<T>) {
        std::mem::swap(&mut self.set, &mut other.set);
    }

    pub fn count(&self, value: T) -> usize {
        if self.set.contains(&value) {
            1
        } else {
            0
        }
    }
}

#[macro_export]
macro_rules! unordered_set {
    () => {
        unordered_set::new()
    };
    ($($item:expr),+ $(,)?) => {
        {
            let mut temp_set = unordered_set::new();
            $(temp_set.insert($item);)*
            temp_set
        }
    };
}
