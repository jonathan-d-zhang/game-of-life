pub mod py_interface;

const fn generate_lookup() -> [u32; 512] {
    let mut lookup = [0; 512];
    let mut i: u32 = 0;
    while i < 512 {
        let center_square = (i >> 4) & 1;
        let ones = i.count_ones() - center_square;
        if center_square == 1 && (ones == 2 || ones == 3) || center_square == 0 && ones == 3 {
            lookup[i as usize] = 1;
        }
        i += 1;
    }
    lookup
}

const LOOKUP: [u32; 512] = generate_lookup();


fn step(alive: Vec<Vec<u32>>) -> Vec<Vec<u32>> {
    let mut res = vec![vec![0; alive[0].len()]; alive.len()];

    let y_len = res.len();
    let x_len = res[0].len();

    for y in 0..y_len {
        let y_left_wrap = match y {0 => y_len - 1, _ => y - 1};
        let y_right_wrap = (y + 1) % y_len;
        let mut c =
            (alive[y_left_wrap][0] << 5) + (alive[y_left_wrap][1] << 4)
            + (alive[y][0] << 3) + (alive[y][1] << 2)
            + (alive[y_right_wrap][0] << 1) + alive[y_right_wrap][1];

        for x in 0..=x_len {
            let x_wrap = (x + 1) % x_len;
            c = ((c % 64) << 3)
                + (alive[y_left_wrap][x_wrap] << 2)
                + (alive[y][x_wrap] << 1)
                + alive[y_right_wrap][x_wrap];

            res[y][x % x_len] = LOOKUP[c as usize];
        }
    }

    res
}
