#! /bin/bash

#$ -j yes
#$ -N predicate_search_job
#$ -o /home/jgualla/vagueness/src/GQA_Data/output_test.json
#$ -l 'mem_free=1M,h_rt=01:00:00'
#$ -m ae -M jgualla1@jh.edu
#$ -cwd

python /home/jgualla1/vagueness/src/GQA_Data/GQA_Predicate_Search.py
