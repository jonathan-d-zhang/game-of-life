pub mod py_interface;

/*
 *
const fn generate_lookup(alive: bool) -> [u8; u8::MAX as usize] {
    let mut lookup = [0; u8::MAX as usize];
    let mut i: u8 = 0;
    while i < u8::MAX {
        let ones = i.count_ones();
        if (alive && ones == 2) || ones == 3 {
            lookup[i as usize] = 1;
        }
        i += 1
    }
    lookup
}
const DEAD_LOOKUP: [u8; u8::MAX as usize] = generate_lookup(false);
const ALIVE_LOOKUP: [u8; u8::MAX as usize] = generate_lookup(true);
*/

const NEIGHBORS: [(i32, i32); 8] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
];

fn step(alive: Vec<Vec<u8>>) -> Vec<Vec<u8>> {
    let mut res = vec![vec![0; alive[0].len()]; alive.len()];

    let y_len = res.len();
    let x_len = res[0].len();

    for y in 0..y_len {
        for x in 0..x_len {
            let mut c = 0;

            for &(dx, dy) in NEIGHBORS.iter() {
                let ny = (y as i32 + dy).rem_euclid(y_len as i32) as usize;
                let nx = (x as i32 + dx).rem_euclid(x_len as i32) as usize;
                if alive[ny][nx] == 1 {
                    c += 1;
                }
            }
            let prev_alive = alive[y][x] == 1;
            if (prev_alive && (c == 2 || c == 3)) || (!prev_alive && c == 3) {
                res[y][x] = 1;
            }
        }
    }

    res
}