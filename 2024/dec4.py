import numpy as np
from dec3 import get_matches_and_idx

def get_input(input_path):

    with open(input_path, 'r') as f:
        text = f.read()

    # text = """
    # MMMSXXMASM
    # MSAMXMSMSA
    # AMXSXMAAMM
    # MSAMASMSMX
    # XMASAMXAMM
    # XXAMMXXAMA
    # SMSMSASXSS
    # SAXAMASAAA
    # MAMMMXMMMM
    # MXMXAXMASX
    # """

    return text

# -----------------------------------------------
def process_text(text):
    lines = text.strip().replace(' ','').split("\n")
    matrix = [list(l) for l in lines]
    return np.array(matrix)

# -----------------------------------------------
def get_diagonals(m):
    nr, nc = m.shape
    diagonals = []
    for o in range(-nr+1, nc):
        d = m.diagonal(o).tolist()
        diagonals.append(d)
    return diagonals

# -----------------------------------------------
def flip(m):
    if type(m) == np.ndarray:
        return np.flip(m, axis=1)
    else:
        mr = [row[::-1] for row in m]
        return mr

# -----------------------------------------------
def search_matrix(m, pattern):
    m_idx = []
    n = 0
    for l in m:
        ls = ''.join(l)
        matches, match_idx = get_matches_and_idx(pattern,ls)
        m_idx.append(match_idx)
        n += len(matches)

    return n, m_idx


# -----------------------------------------------
def part_1(text):

    m = process_text(text)
    mT = m.T
    md = get_diagonals(m)
    mrd = get_diagonals(np.fliplr(m))

    sets = [m, mT, md, mrd]
    n = 0
    for a in sets:
        n += search_matrix(a,'XMAS')[0]
        n += search_matrix(flip(a),'XMAS')[0]

    print(f"Part 1: XMAS count = {n}")
    return


# -----------------------------------------------
def part_2(text):

    m = process_text(text)
    n_rows, n_cols = m.shape

    n = 0
    for i in range(1, n_rows-1, 1):
        for j in range(1, n_cols-1, 1):

            c, tl, tr, bl, br = (
                m[i][j],
                m[i-1][j-1],
                m[i-1][j+1],
                m[i+1][j-1],
                m[i+1][j+1],
            )

            if c  != 'A': continue

            lr_mas = ((tl == 'M') & (br == 'S')) | ((tl == 'S') & (br == 'M'))
            rl_mas = ((tr == 'M') & (bl == 'S')) | ((tr == 'S') & (bl == 'M'))


            if lr_mas & rl_mas : 
                n += 1

    print(f"Part 2: X-MAS count = {n}")
    return

# -----------------------------------------------
def main():
    input_path = './input/dec4_input.txt'
    text = get_input(input_path)
    part_1(text)
    part_2(text)

# -----------------------------------------------
if __name__ == "__main__":
    main()
