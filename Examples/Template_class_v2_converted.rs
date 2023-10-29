#![allow(warnings, unused)]
// Templates are not yet fully supported for conversion
#[derive(Default)]
pub struct TemplExample<T> {
    obj: T,
    size: i32,
}
// Templates are not yet fully supported for conversion
impl<T> TemplExample<T> {
    fn new(mut o: T, mut s: i32) -> TemplExample<T> {
        obj = o as i32;
        size = s;
        let mut i: i32 = 0 as i32;
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
}
// Templates are not yet fully supported for conversion
impl<T> TemplExample<T> {
    fn print(&mut self) {
        std::println!(" {}", self.obj);
    }
}
