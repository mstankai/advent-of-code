import numpy as np

def get_input(input_path):

    with open(input_path, 'r') as f:
        text = f.read()

    # text = """
    # 47|53
    # 97|13
    # 97|61
    # 97|47
    # 75|29
    # 61|13
    # 75|53
    # 29|13
    # 97|29
    # 53|29
    # 61|53
    # 97|53
    # 61|29
    # 47|13
    # 75|47
    # 97|75
    # 47|61
    # 75|61
    # 47|29
    # 75|13
    # 53|13

    # 75,47,61,53,29
    # 97,61,53,29,13
    # 75,29,13
    # 75,97,47,61,53
    # 61,13,29
    # 97,13,75,29,47
    # """

    return text


# -----------------------------------------------
def process_text(text):

    rules = []
    updates = []

    lines = text.strip().replace(' ','').split("\n")

    rules = [ l.split('|') for l in lines if '|' in l]
    updates = [l.split(',') for l in lines if ',' in l]

    return rules, updates

# -----------------------------------------------
def sort_updates(rules, updates):
    good, bad = [], []

    for u in updates:
        ok = True
        for i, page in enumerate(u):
            if not ok: break

            in_front = u[:i]            
            if not in_front: continue
            
            for r in rules:
                if r[0] != page: continue
                if r[1] in in_front :
                    ok = False
                    break

        if ok : 
            good.append(u)
        else:
            bad.append(u)
        
    return good, bad

# -----------------------------------------------
def move_item(l, from_idx, to_idx):
    item = l.pop(from_idx)
    l.insert(to_idx, item)
    return l
# -----------------------------------------------
def part_1(good_updates):
    
    middle_pages = [ (u[len(u)//2]) for u in good_updates ]
    sum_middles = np.array(middle_pages).astype(int).sum()
    print(f"Part 1: sum of the middle pages of good updates = {sum_middles}")
    return

# -----------------------------------------------
def part_2(rules, updates):

    middle_pages = []

    for u in updates: 
        i = 0 
        while i < len(u):
            change = False
            page = u[i]
            in_front = u[:i]

            if not in_front : 
                i += 1
                continue

            for r in rules:
                if r[0] != page: continue
                if r[1] in in_front :
                    i_to = u.index(r[1])
                    move_item(u, i, i_to)
                    change = True
                    break
            
            if change:
                i = i_to
            else:
                i += 1
                if i == len(u) :
                    middle_pages.append(u[len(u)//2])
            
    sum_middles = np.array(middle_pages).astype(int).sum()
    print(f"Part 2: sum of the middle pages of fixed updates = {sum_middles}")

# -----------------------------------------------
def main():
    input_path = './input/dec5_input.txt'
    text = get_input(input_path)
    rules, updates = process_text(text)
    good, bad = sort_updates(rules, updates)
    part_1(good)
    part_2(rules, bad)

# -----------------------------------------------
if __name__ == "__main__":
    main()
