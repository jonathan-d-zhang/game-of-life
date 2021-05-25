use cpython::{PyResult, PySet};
use std::collections::HashSet;

pub mod py_interface;

fn step(alive: HashSet<(i32, i32)>) -> HashSet<(i32, i32)> {
    let mut res = HashSet::new();

    res
}
