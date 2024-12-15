import re
import numpy as np

def get_input(input_path):

    with open(input_path, 'r') as f:
        text = f.read()

    # text = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    # text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    return text

# -----------------------------------------------
def get_prod_from_mult(m_str):
    d_strings = re.findall(r'\d+',m_str)
    digits = np.array([int(d) for d in d_strings])
    prod = np.prod(digits)
    return prod 

# -----------------------------------------------
def get_matches_and_idx(pattern, text):
    matches = re.finditer(pattern,text)

    m_str, m_idx = [],[]
    for m in matches:
        m_str.append(m.group())
        m_idx.append(m.start())

    return m_str, m_idx


# -----------------------------------------------
def part_1(text):
    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern,text)
    
    total = 0
    for m in matches:
        prod = get_prod_from_mult(m)
        total += prod

    print(f"Part 1: Multiplication sum = {total}")

    return
# -----------------------------------------------
def part_2(text):
    p1 = r"mul\(\d+,\d+\)"
    p2 = r"do\(\)"
    p3 = r"don't\(\)"
    
    matches = []
    indexes = []

    for p in [p1,p2,p3]:
        m, i = get_matches_and_idx(p,text)
        matches += m
        indexes += i
    
    m_zip = zip(indexes,matches)
    sorted_zip = sorted(m_zip)

    dont = False
    total = 0
    for i, m in sorted_zip:
        if "don't" in m:
            dont = True
            continue
        if "do" in m:
            dont = False
            continue

        if dont == True:
            continue

        total += get_prod_from_mult(m)
    
    print(f"Part 2: Multiplication sum with conditionals = {total}")

    return

# -----------------------------------------------
def main():
    input_path = './dec3/input.txt'
    text = get_input(input_path)
    part_1(text)
    part_2(text)

# -----------------------------------------------
if __name__ == "__main__":
    main()
