use cpython::PyResult;
use cpython::{py_fn, py_module_initializer, Python};

py_module_initializer!(game_of_life, |py, m| {
    m.add(py, "step", py_fn!(py, step(points: Vec<Vec<u8>>)))?;
    Ok(())
});

fn step(_: Python, points: Vec<Vec<u8>>) -> PyResult<Vec<Vec<u8>>> {
    let res = super::step(points);
    Ok(res)
}