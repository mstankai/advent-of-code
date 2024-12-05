import numpy as np 
import pandas as pd
import sys


def get_records(input_path):

    records = []
    with open(input_path, 'r') as f:
        for line in f:
            r = [int(v) for v in line.split(' ')]
            records.append(r)

    # records = [
    #     [7, 6, 4, 2, 1], 
    #     [1, 2, 7, 8, 9], 
    #     [9, 7, 6, 2, 1], 
    #     [1, 3, 2, 4, 5], 
    #     [8, 6, 4, 4, 1], 
    #     [1, 3, 6, 7, 9]
    # ]

    return records

# -----------------------------------------------
def is_safe(irecord):
    record = np.array(irecord)
    difs = np.diff(record)

    is_sorted = np.all(difs > 0) or np.all(difs < 0)

    if not is_sorted:
        return False
    
    abs_difs = np.abs(difs)
    
    if abs_difs.max() > 3:
        return False

    return True

# -----------------------------------------------
def is_safe_with_dampener(record):

    if is_safe(record):
        return True

    for i in range(len(record)):
        r = record[:i] + record[i+1:]
        safe = is_safe(r)
        if safe:
            return True

    return False    


# -----------------------------------------------
def part_1(records):
    n_safe = 0
    for r in records:
        if is_safe(r):
            n_safe += 1
    print(f"Part 1: # safe reports = {n_safe}")

# -----------------------------------------------
def part_2(records):
    n_safe = 0
    for r in records:
        if is_safe_with_dampener(r):
            n_safe += 1

    print(f"Part 2: # safe reports with dampener = {n_safe}")

# -----------------------------------------------
def main():
    input_path = './input/dec2_input.txt'
    records = get_records(input_path)
    part_1(records)
    part_2(records)

# -----------------------------------------------
if __name__ == "__main__":
    main()
