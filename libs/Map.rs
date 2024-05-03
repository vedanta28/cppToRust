use std::collections::btree_map::Iter;
use std::collections::btree_map::Range;
use std::collections::BTreeMap;
use std::ops::Bound::Included;
use std::ops::Index;

#[derive(Clone, PartialEq, Eq, PartialOrd, Ord, Debug)]
pub struct map<T: Ord, K> {
    pub data: BTreeMap<T, K>,
}

impl<T: Ord, K> map<T, K> {
    pub fn new() -> Self {
        map {
            data: BTreeMap::new(),
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

    pub fn empty(&self) -> bool {
        self.data.is_empty()
    }

    pub fn size(&self) -> usize {
        self.data.len()
    }

    pub fn max_size(&self) -> usize {
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

    pub fn swap(&mut self, other: &mut map<T, K>) {
        std::mem::swap(&mut self.data, &mut other.data);
    }

    pub fn count(&self, key: T) -> usize {
        let contains = self.data.contains_key(&key);
        match contains {
            true => 1,
            false => 0,
        }
    }

    pub fn equal_range(&self, key: T) -> Range<T, K> {
        self.data.range((Included(&key), Included(&key)))
    }

    pub fn lower_bound(&self, key: T) -> Iter<T, K> {
        let mut iter = self.data.iter();
        while let Some((k, v)) = iter.next() {
            if k >= &key {
                return iter;
            }
        }
        iter
    }

    pub fn upper_bound(&self, key: T) -> Iter<T, K> {
        let mut iter = self.data.iter();
        while let Some((k, v)) = iter.next() {
            if k > &key {
                return iter;
            }
        }
        iter
    }

    // This uses nightly-only experimental API, so commented out for now
    // pub fn lower_bound(&self, key: T) -> Cursor<'_, T, K> {
    //     map.lower_bound(Bound::Included(&key))
    // }
    //
    // pub fn uppwer_bound(&self, key: T) -> Cursor<'_, T, K> {
    //     map.upper_bound(Bound::Included(&key))
    // }

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
macro_rules! map {
    () => {
        BTreeMap::new()
    };
    ({}) => {
        BTreeMap::new()
    };
    ({$key:expr, $value:expr} $( , {$key2:expr, $value2:expr})*) => {
        {
            let map =  BTreeMap::new();
            map.insert($key,$value);
            $(map.insert($key2,$value2);)*
            map
        }
    };
}

// Index trait implementation
impl<T: Ord, K> Index<T> for map<T, K> {
    type Output = K;

    fn index(&self, index: T) -> &K {
        &self.data[&index]
    }
}
