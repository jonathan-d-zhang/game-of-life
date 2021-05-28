pub mod py_interface;

const fn generate_alive_lookup() -> [u8; u8::MAX as usize] {
    let mut lookup = [0; u8::MAX as usize];
    let mut i: u8 = 0;
    while i < u8::MAX {
        let ones = i.count_ones();
        if ones == 2 || ones == 3 {
            lookup[i as usize] = 1;
        }

        i += 1
    }

    lookup
}

const fn generate_dead_lookup() -> [u8; u8::MAX as usize] {
    let mut lookup = [0; u8::MAX as usize];
    let mut i: u8 = 0;
    while i < u8::MAX {
        if i.count_ones() == 3 {
            lookup[i as usize] = 1;
        }

        i += 1
    }

    lookup
}
const DEAD_LOOKUP: [u8; u8::MAX as usize] = generate_dead_lookup();
const ALIVE_LOOKUP: [u8; u8::MAX as usize] = generate_alive_lookup();

fn step(alive: Vec<Vec<u8>>) -> Vec<Vec<u8>> {
    let mut res = vec![vec![0; alive[0].len()]; alive.len()];

    res
}
