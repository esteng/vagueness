from glob import glob
import numpy as np
import os 
np.random.seed(12) 

MAX_LINES = 16

output_path = "data/gqa/csv/outputs_csv_subset"

for filename in glob("data/gqa/csv/outputs_csv_small_corrected/*"):
    with open(filename) as f1:
        lines = f1.readlines()
        header = lines[0]
        lines = lines[1:]
    if len(lines) < MAX_LINES:
        subset_lines = lines 
    else:
        subset_lines = np.random.choice(lines, MAX_LINES) 

    subset_lines = [x for x in subset_lines]
    subset_lines = [header] + subset_lines
    with open(os.path.join(output_path, os.path.basename(filename)), "w") as f1:
        for line in subset_lines:
            f1.write(line.strip() + "\n") 

       
