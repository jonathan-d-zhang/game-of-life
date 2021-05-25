use cpython::{py_fn, py_module_initializer, Python};
use cpython::{PyNone, PyResult, PySet};

py_module_initializer!(game_of_life, |py, m| { Ok(()) });

fn mut_set(py: Python, set: PySet) -> PyResult<PyNone> {
    set.add(py, (-10, 10))?;
    Ok(PyNone)
}
