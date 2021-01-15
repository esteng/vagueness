#!/bin/bash

#$ -j yes
#$ -N predicate_search_job
#$ -o /home/jgualla1/vagueness/src/vqa/nonvague_questions.json
#$ -l 'mem_free=1M,h_rt=01:00:00'
#$ -m ae -M jgualla1@jh.edu
#$ -cwd

python /home/jgualla1/vagueness/src/vqa/vqa_predicate_search.py





