use cpython::{py_fn, py_module_initializer, Python};
use cpython::{PyNone, PyResult, PySet};
use std::collections::HashSet;

py_module_initializer!(game_of_life, |py, m| {
    m.add(py, "mut_set", py_fn!(py, mut_set(set: PySet)))?;
    m.add(py, "step", py_fn!(py, step(points: Vec<(i8, i8)>)))?;
    Ok(())
});

fn mut_set(py: Python, set: PySet) -> PyResult<PyNone> {
    set.add(py, (-10, 10))?;
    Ok(PyNone)
}

fn step(_: Python, points: Vec<(i8, i8)>) -> PyResult<Vec<(i8, i8)>> {
    let s = points
        .into_iter()
        .collect::<HashSet<_>>();
    let res = super::step(s);
    Ok(res)
}
