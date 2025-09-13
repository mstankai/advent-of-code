import re
import sys
import numpy as np

# -----------------------------------------------
class Item:
    def __init__(self, fid: int, l: int):
        self.fid = fid
        self.len = l
        self.is_file = (fid >= 0)

    def __str__(self):
        if self.is_file:
            return f"File - ID: {self.fid}, size: {self.len}"
        else:
            return f"Space - size: {self.len}"
        
    def viz(self):
        if self.is_file:
            return str(self.fid)*self.len
        else:
            return '.'*self.len

# -----------------------------------------------
def get_input(input_path):

    with open(input_path, 'r') as f:
        text = f.read()

    text = "2333133121414131402"
    # text = "12345"
    return text


# -----------------------------------------------
def get_map_p1(text: str):

    filemap = []

    for i, c in enumerate(text):
        idx = str(i // 2)
        is_file = (i % 2 == 0)
        l = int(c)

        if is_file:
            filemap.extend([idx for j in range(l)])
        else :
            filemap.extend(['.' for j in range(l)])
    
    return filemap

# -----------------------------------------------
def get_map_p2(text: str):

    filemap = []

    for i, c in enumerate(text):
        idx = i // 2
        is_file = (i % 2 == 0)
        l = int(c)

        if is_file:
            filemap.append(Item(idx, l))
        else :
            filemap.append(Item(-1,l))
    
    return filemap

# -----------------------------------------------
def part_1(text):

    m = get_map_p1(text)

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

        # print(" ".join(m))

    # --- get file checksum ---
    cs = 0
    for pos, fid_str  in enumerate(m):
        if fid_str == '.': break
        fid = int(fid_str)
        cs += pos * fid
        # print(pos, fid)
    
    print(f"Part 1, checksum: {cs}")

# -----------------------------------------------
def print_map2(m):
    mp = [i.viz() for i in m]
    print(" ".join(mp))
# -----------------------------------------------
def part_2(text):

    print("Input: ",text)
    m = get_map_p2(text)

    # --- rearrange files ---
    m_orig = m.copy()

    j = len(m) - 1
    jm = len(m) - 1

    while j > 0:
        b = m_orig[j]

        if not b.is_file: 
            j -= 1
            jm -= 1
            continue

        i = 0
        while i <= j: 
            f = m[i]
            if (f.is_file) or (f.len < b.len):
                i += 1
                continue

            # --- move file ---
            print_map2(m)

            print("f: ", f)
            print("b: ", b)
            print("i,j,jm: ",i,j,jm)

            m[jm] = Item(-1, b.len) # make space
            
            diff = f.len - b.len
            if diff == 0:
                m[i] = b
            else:
                m[i:i+1] = [b, Item(-1, diff)]
                jm += 1
            
            j-=1
            jm-=1

            print_map2(m)
            print("-----------")
            break

        j-=1
        jm-=1
    # print(f"Part 2: {total}")
    return

# -----------------------------------------------
def main():
    input_path = './dec9/input.txt'
    text = get_input(input_path)

    # part_1(text)
    part_2(text)

# -----------------------------------------------
if __name__ == "__main__":
    main()
