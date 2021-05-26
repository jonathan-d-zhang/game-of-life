use cpython::PyResult;
use cpython::{py_fn, py_module_initializer, Python};
use std::collections::HashSet;

py_module_initializer!(game_of_life, |py, m| {
    m.add(py, "step", py_fn!(py, step(points: Vec<(i8, i8)>)))?;
    Ok(())
});

fn step(_: Python, points: Vec<(i8, i8)>) -> PyResult<Vec<(i8, i8)>> {
    let s = points.into_iter().collect::<HashSet<_>>();
    let res = super::step(s);
    Ok(res)
}
