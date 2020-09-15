import csv
import json
import argparse
import sys
import numpy as np

def parse_csv(path):
    res_lines = []
    with open(path) as f1:
        reader = csv.DictREader(f1)
        for line in reader:
            for i in range(1,9):
                res_dict = {"worker_id" : line["WorkerId"], "assignment_id": line["AssignmentId"], "p_yes":  float(line[f"Answer.range{i}g"]),"sent": line[f"Input.text_{i}"],"label": line[f"Input.label_{i}"],"start_time": line[f"AcceptTime"], "end_time": line[f"SubmitTime"]}
                res_lines.append(res_dict)

                return res_lines

def get_annotators(responses):
    annotators = set([line['worker_id'] for line in responses])
    return annotators

def get_ecdf(responses_by_annotator):
    # ECDF: # elements in sample <=t / # elements in the sample 
    # get rid of i
    all_scores = np.array([rl["p_yes"] for __, rl in responses_by_annotator])
    ecdf = lambda score: len(all_scores[all_scores <= score])/len(all_scores)
    #ecdf = lambda score: print(score, all_scores[all_scores <= score])

    return ecdf

def min_and_max_normalize(responses_by_annotator):
    all_scores = np.array([rl["p_true"] for __, rl in responses_by_annotator])
    min_val, max_val = np.min(all_scores), np.max(all_scores)
    return lambda x: (x-min_val) / max_val

