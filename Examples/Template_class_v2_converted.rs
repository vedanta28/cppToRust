#![allow(warnings, unused)]
// Templates are not yet fully supported for conversion
#[derive(Default)]
pub struct TemplExample<T> {
    obj: T,
    size: i32,
}
// Templates are not yet fully supported for conversion
impl<T> TemplExample<T> {
    fn TemplExample(mut o: T, mut s: i32) -> TemplExample<T> {
        obj = o;
        size = s;
        let mut i: i32 = 0;
        while i < size {
            obj += o;
            i += 1;
        }
    }
}
// Templates are not yet fully supported for conversion
impl<T> TemplExample<T> {
    fn print() {
        std::println!(" {}", obj);
    }
}
