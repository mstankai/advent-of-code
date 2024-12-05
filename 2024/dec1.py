import numpy as np 
import pandas as pd

input_path = './input/dec1_input.txt'

l1, l2 = [], []
with open(input_path, 'r') as f:
    for line in f:
        i, j = line.split('   ')
        l1.append(int(i))
        l2.append(int(j))


# l1 = [3,4,2,1,3,3,]
# l2 = [4,3,5,3,9,3,]

# ------------ part 1 -----------------

sl1 = sorted(l1)
sl2 = sorted(l2)

dists = np.array([
    abs(a - b) 
    for a,b in zip(sl1,sl2)
])

total_dist = dists.sum()
print(f"Part 1: distance = {total_dist}")


# ------------ part 2 -----------------

def get_fqs(l):
    df = pd.DataFrame(columns=['n'], data=l)
    fqs_dict = df.n.value_counts().to_dict()
    return fqs_dict

l1_fqs = get_fqs(sl1)
l2_fqs = get_fqs(sl2)

sim_score = 0
for n, fq in l1_fqs.items():
    if n not in l2_fqs: continue
    sim_score += (n * fq * l2_fqs[n])

print(f"Part 1: similarity score = {sim_score}")
