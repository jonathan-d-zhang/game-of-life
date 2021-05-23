use cpython::{PyResult, Python, py_module_initializer, py_fn};

py_module_initializer!(game_of_life, |py, m| {
    m.add(py, "add", py_fn!(py, add(a: u32, b: u32)))?;
    Ok(())
});

fn add(_: Python, a: u32, b: u32) -> PyResult<u32> {
    Ok(super::add(a, b))
}
