from dataclasses import dataclass

# -----------------------------------------------
def get_input(input_path):

    with open(input_path, 'r') as f:
        text = f.read()

    text = "2333133121414131402"
    # text = "12345"
    return text


# -----------------------------------------------
# PART 1
# we treat the map as a list with numbers and spaces ('.')

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

# -------
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
# PART 2
# we treat files and spaces as items (new class)

@dataclass
class Item:
    pos: int
    fid: int
    size: int

    @property 
    def is_file(self):
        return self.fid >= 0

    @property
    def end(self):
        return self.pos + self.size
        
    def viz(self):
        if self.is_file:
            return str(self.fid)*self.size
        else:
            return '.'*self.size
        
    def __str__(self):
        ftype = 'F' if self.is_file else 'S'
        return f"[{ftype}] Pos {self.pos}, ID: {self.fid}, size: {self.size}"


# -------
def get_map_p2(text: str):
    filemap = []
    pos = 0
    for i, c in enumerate(text):
        idx = i // 2
        is_file = (i % 2 == 0)
        l = int(c)
        if l == 0: continue
        if is_file:
            filemap.append(Item(pos, idx, l))
        else :
            filemap.append(Item(pos, -1,l))
        pos += l
    return filemap

# -------
def print_map2(m):
    mp = [i.viz() for i in m]
    print(" ".join(mp))

# -------
def item_pos_sort(m, desc=False):
    sort_key = (lambda x: x.pos)
    return sorted(m, key=sort_key, reverse=desc)

# -------
def merge_spaces(spaces):
    if any(s.is_file for s in spaces):
        raise ValueError("Not all spaces!")
    spaces = item_pos_sort(spaces)
    merged = []
    for s in spaces:
        if merged and merged[-1].end == s.pos:
            merged[-1].size += s.size
        else:
            merged.append(s)
    return merged

# -------
def get_item_checksum(m):
    cs = 0
    for item in m:
        if not item.is_file: continue
        # id * pos for each space file takes up
        vals = [
            (item.pos+i) * item.fid 
            for i in range(item.size)
        ]
        cs += sum(vals)
    return cs

# -------
def part_2(text):
    # could be improved by not doing a full list sort+merge
    # but just addressing adjacent and putting space into place
    # but it works as is

    m = get_map_p2(text)
    # print_map2(m)

    files = [f for f in m if f.is_file]
    spaces = [s for s in m if not s.is_file]

    # loop over reversed files  
    files = item_pos_sort(files, desc=True) 
    for f in files:

        # check if it can fit in any of the spaces
        for s in spaces:
            if s.pos > f.pos: break

            diff = s.size - f.size
            if diff >= 0:
                
                # move file forward
                file_pos = f.pos
                f.pos = s.pos

                # move space back
                s.pos = file_pos
                s.size = f.size

                # if space was larger than file create a new space
                # and add in the same place in space list
                if diff > 0:
                    npos = f.end
                    new_space = Item(npos, -1, diff)
                    spaces.append(new_space)

                # order and merge spaces
                spaces = merge_spaces(spaces)

                # # check sort
                # new_map = item_pos_sort(files + spaces)
                # print_map2(new_map)

                # stop searching                    
                break

    new_map = item_pos_sort(files + spaces)
    cs = get_item_checksum(new_map)

    print(f"Part 2, checksum: {cs}")
    return

# -----------------------------------------------
def main():
    input_path = './dec9/input.txt'
    text = get_input(input_path)

    part_1(text)
    part_2(text)

# -----------------------------------------------
if __name__ == "__main__":
    main()
