use std::collections::HashSet;

pub mod py_interface;

fn neighbors(point: (i8, i8), with_self: bool) -> Vec<(i8, i8)> {
    let (x, y) = point;
    let mut res = Vec::new();
    if with_self {
        res.push((x, y));
    }

    for dx in -1..2 {
        for dy in -1..2 {
            if dx == dy && dy == 0 {
                continue;
            }
            res.push((x + dx, y + dy));
        }
    }

    res
}

fn step(alive: HashSet<(i8, i8)>) -> HashSet<(i8, i8)> {
    let mut seen = HashSet::new();
    let mut flipping = HashSet::new();

    for cell in alive.iter() {
        for neighbor in neighbors(*cell, true) {
            if seen.contains(&neighbor) {
                continue;
            }
            seen.insert(neighbor);

            let s = neighbors(neighbor, false)
                .iter()
                .filter(|c| alive.contains(c))
                .count();

            if alive.contains(&neighbor) && (s != 2 && s != 3)
                || !alive.contains(&neighbor) && (s == 3)
            {
                flipping.insert(neighbor);
            }
        }
    }

    let mut temp = HashSet::new();
    for cell in alive.iter() {
        if !flipping.contains(cell) {
            temp.insert(*cell);
        }
    }
    for cell in flipping.iter() {
        if !alive.contains(cell) {
            temp.insert(*cell);
        }
    }

    temp
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_neighbor_with_self() {
        let res = vec![
            (0, 0),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ];
        assert_eq!(res, neighbors((0, 0), true));
    }

    #[test]
    fn test_neighbor() {
        let res = vec![
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ];
        assert_eq!(res, neighbors((0, 0), false));
    }
}
