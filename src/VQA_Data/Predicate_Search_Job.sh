#!/bin/bash

#$ -j yes
#$ -N predicate_search_job
#$ -o /home/jgualla1/vagueness/src/VQA_Data/output_old_csv_yesno.csv





#$ -l 'mem_free=1M,h_rt=01:00:00'
#$ -m ae -M jgualla1@jh.edu
#$ -cwd

python /home/jgualla1/vagueness/src/VQA_Data/CSV_Creator.py





