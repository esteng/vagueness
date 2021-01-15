import csv
import json
import argparse
import sys
import numpy as np

def parse_csv(path):
    res_lines = []
    with open(path) as f1:
        reader = csv.DictReader(f1)
        for line in reader: 
            for i in range(1,9):
                try:
                    res_dict = {"worker_id": line["WorkerId"],
                                "assignment_id": line["AssignmentId"],
                                "question_id": line[f"Input.question_id_{i-1}"], 
                                "p_true":  float(line[f"Answer.range{i}g"]),
                                "sent": line[f"Input.question_{i-1}"] + "-" + line[f"Input.imageurl_{i-1}"],
                                "start_time": line[f"AcceptTime"],
                                "end_time": line[f"SubmitTime"]}
                    res_lines.append(res_dict)
                except KeyError:
                    # already parsed 
                    assert("worker_id" in line)
                    line["p_true"] = float(line["p_true"])
                    res_lines.append(line) 
    return res_lines 

def get_annotators(responses):
    annotators = set([line['worker_id'] for line in responses])
    return annotators

def get_ecdf(responses_by_annotator):
    # ECDF: # elements in sample <=t / # elements in the sample 
    # get rid of i
    all_scores = np.array([rl["p_true"] for __, rl in responses_by_annotator])
    ecdf = lambda score: len(all_scores[all_scores <= score])/len(all_scores)
    #ecdf = lambda score: print(score, all_scores[all_scores <= score])

    return ecdf

def min_and_max_normalize(responses_by_annotator):
    all_scores = np.array([rl["p_true"] for __, rl in responses_by_annotator])
    min_val, max_val = np.min(all_scores), np.max(all_scores)
    return lambda x: (x-min_val) / max_val

def normalize(responses):
    for annotator in get_annotators(responses):
        responses_by_annotator = [(i, r) for (i,r) in enumerate(responses) if r['worker_id'] == annotator]
        mm_norm = min_and_max_normalize(responses_by_annotator) 
        for j, (i, line) in enumerate(responses_by_annotator):
            score = line['p_true']
            norm_score = mm_norm(score)
            line["p_true_norm"] = norm_score
            try:
                assert(norm_score >= 0 and norm_score <= 1)
            except AssertionError:
                continue
                #print(norm_score)
                #print(f"norm score is {norm_score}") 
                #print(score)
                #print(mm_norm) 
                #sys.exit()

            responses[i] = line 

    return responses


def ridit_score(responses):
    # ridit =  (y_ai) = ECDF_ya (y_ai − 1) + 0.5 × ECDF_ya (y_ai)
    ridit = {}
    for annotator in get_annotators(responses):
        responses_by_annotator = [(i, r) for (i,r) in enumerate(responses) if r['worker_id'] == annotator]
        ecdf = get_ecdf(responses_by_annotator) 
        for j, (i, line) in enumerate(responses_by_annotator):
            score = line['p_true']
            ridit_score = ecdf(score-1) + 0.5 * ecdf(score)
            line["p_true_ridit"] = ridit_score
            responses[i] = line 

    return responses

def get_decision_one_annotator(res_lines, use_ridit = True):
    if use_ridit:
        dec_key = "p_true_norm"
        dec_val = 0.5
    else:
        dec_key = "p_true"
        dec_val = 50.00

    for i, d_line in enumerate(res_lines):
        ann = d_line["worker_id"]
        p_true = d_line[dec_key]
        if float(p_true) > dec_val:
            answer = "True"
        else:
            answer = "False"
        d_line[f"decision_{ann}"] = answer
        res_lines[i] = d_line
    return res_lines

def vote(res_lines, bad_annotators = [ ]):
    out_dict = []
    for i, d_line in enumerate(res_lines):
        total = 0
        num_na = 0
        any_annotated = False
        for key in d_line:
            if key.startswith("decision"):
                annotator = key.split("_")[1]
                if annotator in bad_annotators:
                #    # skip shitty annotators
                    continue
             
                ann_decision = d_line[key]
                #print(d_line['sent'])
                #print(annotator, ann_decision, d_line['label'])
                if ann_decision == "True":
                    total += 1
                    any_annotated = True
                if ann_decision == "False":
                    total += -1
                    any_annotated = True
                else:
                    #N/A
                    num_na += 1
        # only add if we can salvage something 
        if any_annotated:
            d_line["voted_decision"]  = "True" if total > 0 else "False"
            d_line["num_na"] = num_na
            out_dict.append( d_line)
    return out_dict 

def get_accuracy(res_lines, exclude, do_normalize):
    if exclude:
        with open("bad.csv") as f1:
            bad_annotators = f1.read().strip().split(",")
    else:
        bad_annotators = []
    total_true = 0 
    #res_lines = ridit_score(res_lines)
    if do_normalize:
        res_lines = normalize(res_lines)

    res_lines = get_decision_one_annotator(res_lines, use_ridit = do_normalize)
    res_lines = vote(res_lines, bad_annotators)
    return data_summary(res_lines)

def data_summary(lines):
    anns = get_annotators(lines)
    num_anns = len(anns)
    anns_by_acc = []
    for ann in anns:
        responses_by_annotator = [ r for r in lines  if r['worker_id'] == ann]
        res = {"correct_true": 0, "incorrect_true": 0, "correct_false":0,
                "incorrect_false":0, "no_move": 0, "dont_know": 0}
        for line in responses_by_annotator:
            if line['voted_decision'] == 'True' and line['p_true'] > 50.0:
                res['correct_true'] += 1
            elif line['voted_decision'] == "True" and line['p_true'] < 50.0: 
                res['incorrect_true'] += 1
            elif line['voted_decision'] == "False" and line['p_true'] < 50.0: 
                res['correct_false'] += 1
            elif line['voted_decision'] == "False" and line['p_true'] > 50.0: 
                res['incorrect_false'] += 1
            elif line['p_true'] == 50.0:
                res['no_move'] += 1

        print(f"{ann}: {res}")
        annotator_accuracy = (res['correct_true'] + res['correct_false']) / (res['correct_true'] + res['correct_false'] + res['incorrect_true'] + res['incorrect_false'] + res['no_move'] + res['dont_know'])
        anns_by_acc.append((ann, annotator_accuracy)) #, res['correct_true'] + res['correct_false']))
    anns_by_acc = sorted(anns_by_acc, key=lambda x: x[1])
    print(anns_by_acc)
    print(f"macro avg: {np.mean([x[1] for x in anns_by_acc])}")
    #print(",".join([x[0] for x in anns_by_acc if x[1] < 0.501]))
    return anns_by_acc

def filter_data(res_lines, anns_by_acc, output_path, do_normalize): 
    if do_normalize:
        res_lines = normalize(res_lines)
    # get annotators with low accuracy 
    exclude = []
    for ann, acc in anns_by_acc:
        if acc < 0.75:
            # add them to exclusion list 
            exclude.append(ann)
    # exclude exclusion list 
    new_rows = [row for row in res_lines if row["worker_id"] not in exclude]
    with open(output_path, "w") as f1:
        fieldnames = [k for k in new_rows[0].keys() if not k.startswith("decision")]
        writer = csv.DictWriter(f1, fieldnames = fieldnames)
        writer.writeheader() 
        for row in new_rows:
            writer.writerow({k:v for (k,v) in row.items() if k in fieldnames} ) 


def main(args):
    parsed_csv_lines = parse_csv(args.csv)
    anns_by_acc = get_accuracy(parsed_csv_lines, args.exclude, args.normalize)

    if args.produce_csv is not None: 
        filtered = filter_data(parsed_csv_lines, 
                               anns_by_acc, 
                               args.produce_csv, 
                               args.normalize) 
        print(f"filtered csv written to {args.produce_csv}") 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help = "path to MT results", required = True)
    parser.add_argument("--exclude", action="store_true", required = False, help = "set to exclude unreliable annotators (in bad.csv)")
    parser.add_argument("--normalize", action="store_true", required = False, help = "set to normalize data" ) 
    parser.add_argument("--produce-csv", help = "path to produce a filtered csv with normalied scores and no bad annotators", required=False) 
    args = parser.parse_args()
    main(args)
