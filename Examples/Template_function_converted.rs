// Templates are not yet supported for conversion
fn myMax<T, R>(mut x: T, mut y: R) -> T {
    return if (x > y) { x } else { y };
}
