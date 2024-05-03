use std::cmp::Ordering;
use std::collections::BTreeSet;

#[derive(Clone, PartialEq, Eq, PartialOrd, Ord, Debug)]
pub struct set<T> {
    set: BTreeSet<T>,
}

impl<T: Ord> set<T> {
    pub fn new() -> Self {
        set {
            set: BTreeSet::new(),
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

    pub fn insert(&mut self, value: T) {
        self.set.insert(value);
    }

    pub fn erase(&mut self, value: T) {
        self.set.remove(&value);
    }

    pub fn swap(&mut self, other: &mut set<T>) {
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
macro_rules! set {
    () => {
        set::new()
    };
    ($($item:expr),+ $(,)?) => {
        {
            let mut temp_set = set::new();
            $(temp_set.insert($item);)*
            temp_set
        }
    };
}
