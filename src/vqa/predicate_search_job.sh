#!/bin/bash

#$ -j yes
#$ -N predicate_search_job
#$ -o /home/jgualla1/vagueness/src/vqa/output_young_csv_yesno_checked.csv
#$ -l 'mem_free=1M,h_rt=01:00:00'
#$ -m ae -M jgualla1@jh.edu
#$ -cwd

python /home/jgualla1/vagueness/src/vqa/CSV_Creator.py





