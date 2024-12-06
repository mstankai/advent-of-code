import numpy as np
import re
import sys
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
    r, c = m.shape
    
    # get a dummy array with indexes
    m_dummy = []
    for ir in range(r):
        r_dummy = []
        for ic in range(c):
            r_dummy.append((ir*c)+ic)
        m_dummy.append(r_dummy)
    m_dummy = np.array(m_dummy)

    # get diagonals
    md = get_diagonals(m)
    mrd = get_diagonals(np.fliplr(m))

    # get dummy diagonals
    md_dummy = get_diagonals(m_dummy)
    mrd_dummy = get_diagonals(np.fliplr(m_dummy))
    
    # all matrices to run over
    matrices = [md, flip(md), mrd, flip(mrd)]
    dummies = [md_dummy, flip(md_dummy), mrd_dummy, flip(mrd_dummy)]


    # find indices of 'a's of 'MAS' foind in any of the matrices
    a_true_indexes_all = []
    for matrix, dummy in zip(matrices, dummies):
        # get the positions of matches within each line
        match_line_positions = search_matrix(matrix, 'MAS')[1]
        # get the positions of 'A'
        a_line_positions = [[i + 1 for i in l] for l in match_line_positions]

        # get true indexes of the 'a's
        a_true_indexes = []
        for a_found_in_line, true_idx_line in zip(a_line_positions, dummy):
            if len(a_found_in_line) == 0 : continue

            for ia in a_found_in_line:
                a_true_indexes.append(true_idx_line[ia])
        
        a_true_indexes_all.append(a_true_indexes)

    # get the a indexes from different diagonal directions
    a_true_lc = a_true_indexes_all[:2]
    a_true_rc = a_true_indexes_all[2:]


    # check for overlaping 'a's between the two directions
    n = 0
    for lc in a_true_lc:
        for rc in a_true_rc:
            n += len(set(lc).intersection(set(rc)))
    
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
