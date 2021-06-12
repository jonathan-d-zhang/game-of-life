use cpython::PyResult;
use cpython::{py_fn, py_module_initializer, Python};

py_module_initializer!(game_of_life, |py, m| {
    m.add(py, "step", py_fn!(py, step(points: Vec<Vec<u32>>)))?;
    Ok(())
});

fn step(_: Python, points: Vec<Vec<u32>>) -> PyResult<Vec<Vec<u32>>> {
    let res = super::step(points);
    Ok(res)
}
