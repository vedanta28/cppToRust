use std::collections::hash_map::Iter;
use std::collections::HashMap;
use std::ops::Index;

#[derive(Clone, PartialEq, Eq, Debug)]
pub struct unordered_map<T: Ord + std::hash::Hash, K> {
    pub data: HashMap<T, K>,
}

impl<T: Ord + std::hash::Hash, K> unordered_map<T, K> {
    pub fn new() -> Self {
        unordered_map {
            data: HashMap::new(),
        }
    }

    pub fn begin(&self) -> Iter<T, K> {
        self.data.iter()
    }

    pub fn end(&self) -> Iter<T, K> {
        let mut iter = self.data.iter();
        while let Some((k, v)) = iter.next() {}
        iter
    }

    pub fn at(&self, index: &T) -> &K {
        self.data.get(index).unwrap()
    }

    pub fn empty(&mut self) -> bool {
        self.data.is_empty()
    }

    pub fn size(&mut self) -> usize {
        self.data.len()
    }

    pub fn max_size(&mut self) -> usize {
        self.data.len()
    }

    pub fn clear(&mut self) {
        self.data.clear();
    }

    pub fn insert(&mut self, (key, value): (T, K)) {
        self.data.insert(key, value);
    }

    pub fn emplace(&mut self, (key, value): (T, K)) {
        self.data.insert(key, value);
    }

    pub fn erase(&mut self, key: T) -> usize {
        let key = self.data.remove(&key);
        match key {
            None => 0,
            Some(_) => 1,
        }
    }

    pub fn swap(&mut self, other: &mut unordered_map<T, K>) {
        std::mem::swap(&mut self.data, &mut other.data);
    }

    pub fn count(&self, key: T) -> usize {
        let contains = self.data.contains_key(&key);
        match contains {
            true => 1,
            false => 0,
        }
    }

    pub fn equal_range(&self, key: T) -> (Iter<T, K>, Iter<T, K>) {
        let mut iter = self.find(key);
        match iter.next() {
            Some(first) => {
                let mut second = iter.clone();
                second.next();
                return (iter, second);
            }
            None => (iter.clone(), iter),
        }
    }

    pub fn find(&self, key: T) -> Iter<T, K> {
        let mut iter = self.data.iter();
        while let Some((k, v)) = iter.next() {
            if k == &key {
                return iter;
            }
        }
        iter
    }
}

// List initialization macro
#[macro_export]
macro_rules! unordered_map {
    () => {
        HashMap::new()
    };
    ({}) => {
        HashMap::new()
    };
    ({$key:expr, $value:expr} $( , {$key2:expr, $value2:expr})*) => {
        {
            let map =  HashMap::new();
            map.insert($key,$value);
            $(map.insert($key2,$value2);)*
            map
        }
    };
}

// Index trait implementation
impl<T: Ord + std::hash::Hash, K> Index<T> for unordered_map<T, K> {
    type Output = K;

    fn index(&self, index: T) -> &K {
        &self.data[&index]
    }
}
