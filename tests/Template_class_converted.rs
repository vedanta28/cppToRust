#![allow(warnings, unused)]
// Templates are not yet fully supported for conversion
#[derive(Default)]
pub struct TemplExample<T> {
    obj: T,
    size: i32,
}
impl<T> TemplExample<T> {
    pub fn new(mut o: T, mut s: i32) -> TemplExample<T> {
        obj = o;
        size = s;
        let mut i: i32 = 0;
        while i < size {
            obj += o;
            i += 1;
        }

        /*
            This is a constructor method.
            Please appropriate members to the struct constructor as per your logic.
            Currently the constructor returns a struct with all the defaults for the data types in the struct.
        */
        TemplExample {
            ..Default::default()
        }
    }
    pub fn print(&mut self) {
        std::println!(" {}", self.obj);
    }
}
fn main() {}
