use cpython::PyResult;
use cpython::{py_fn, py_module_initializer, Python};

py_module_initializer!(game_of_life, |py, m| {
    m.add(py, "step", py_fn!(py, step(points: Vec<(i32, i32)>)))?;
    Ok(())
});

fn step(_: Python, points: Vec<(i32, i32)>) -> PyResult<Vec<(i32, i32)>> {
    let s = points.into_iter().collect();
    let res = super::step(s).into_iter().collect();
    Ok(res)
}
