import math as m
import numpy as np

def get_input(input_path):

    with open(input_path, 'r') as f:
        text = f.read()

    # text = """
    # 190: 10 19
    # 3267: 81 40 27
    # 83: 17 5
    # 156: 15 6
    # 7290: 6 8 6 15
    # 161011: 16 10 13
    # 192: 17 8 14
    # 21037: 9 7 18 13
    # 292: 11 6 16 20
    # """

    return text
# -----------------------------------------------
def process_text(text):
    lines = text.strip().split("\n")

    test_values = []
    numbers = []
    for l in lines:
        s1, s2 = l.split(':')
        t = int(s1)
        nums = np.array([
            int(n) 
            for n in s2.split(' ') 
            if n.isdigit()
        ])

        test_values.append(t)
        numbers.append(nums)        

    return test_values, numbers

# -----------------------------------------------
def correct_eq(answ, parts, operators):
    n = len(parts)
    
    # create recursive operation
    def apply_operation(i, current_total):
        
        # break branch if too large
        if current_total > answ:
            return False
        
        # check end condition
        if i == len(parts): 
            return (current_total == answ)
        
        # if not end, apply operation to the next value
        next_val = parts[i]
        for o in operators:
            o_is_good = apply_operation(i+1, o(current_total,next_val))
            if o_is_good : return True

        return False

    return apply_operation(1, parts[0])

# -----------------------------------------------
def get_answer(text, operators):
    test_vals, equation_parts = process_text(text)
    correct_test_vals = []
    for t, vals in zip(test_vals, equation_parts):
        if correct_eq(t, vals, operators):
            correct_test_vals.append(t)
    return np.sum(np.array(correct_test_vals))

# -----------------------------------------------
# sligthly faster than (lambda x,y: int(f"{x}{y}"))
def concat(x,y):
    if y == 0:
        return x*10
    len_y = m.floor(m.log10(y)) + 1
    return x * (10**len_y) + y

# -----------------------------------------------
def part_1(text):
    operators = [
        (lambda x,y: x+y),
        (lambda x,y: x*y)
    ]
    print(f"Running part 1 ...")
    calib_val = get_answer(text, operators)
    print(f"Part 1: calibration value = {calib_val}\n")

# -----------------------------------------------
def part_2(text):
    operators = [
        (lambda x,y: x+y),
        (lambda x,y: x*y),
        concat
    ]
    print(f"Running part 2 ...") 
    calib_val = get_answer(text, operators)
    print(f"Part 2: calibration value = {calib_val}")


# -----------------------------------------------
def main():
    input_path = './dec7/input.txt'
    text = get_input(input_path)
    part_1(text)
    part_2(text)

# -----------------------------------------------
if __name__ == "__main__":
    main()
