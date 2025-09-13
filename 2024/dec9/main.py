import re
import sys
import numpy as np

# -----------------------------------------------
def get_input(input_path):

    with open(input_path, 'r') as f:
        text = f.read()

    text = "2333133121414131402"
    # text = "12345"
    return text

# -----------------------------------------------
def get_map_str(text: str):

    fs = ''

    for i, c in enumerate(text):
        idx = str(i // 2)
        is_file = (i % 2 == 0)
        l = int(c)
        if is_file:
            fs += idx*l
        else :
            fs += '.'*l
    
    return fs

# -----------------------------------------------
def part_1(m):


    # --- rearrange files ---
    i, j = 0, len(m) - 1

    while i < j :
        if m[i] != '.':
            i += 1
            continue
        
        if m[j] == '.':
            j -= 1
            continue

        m[i] = m[j]
        m[j] = "."

        i += 1
        j -= 1

        print("".join(m))

    # --- get file checksum ---
    cs = 0
    for pos, fid_str  in enumerate(m):
        if fid_str == '.': break
        fid = int(fid_str)
        cs += pos * fid
    
    print(f"Part 1, checksum: {cs}")

# -----------------------------------------------
def part_2(text):

    # print("Input: ",text)
    # print("Files: ", map_str)
    # print(f"Part 2: {total}")
    return

# -----------------------------------------------
def main():
    input_path = './dec9/input.txt'
    text = get_input(input_path)
    map_str = get_map_str(text)
    m = list(map_str)
    print("Filesystem size: ",len(m))

    part_1(m)
    # part_2(text)

# -----------------------------------------------
if __name__ == "__main__":
    main()
