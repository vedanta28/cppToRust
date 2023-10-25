#![allow(warnings, unused)]
fn main() {
    let mut num = 5;
    let mut add_num_by_val = move |mut x: i32| {
        return x + num;
    };
    let mut add_num_by_ref = |mut x: i32| -> i32 {
        return x + num;
    };
}
