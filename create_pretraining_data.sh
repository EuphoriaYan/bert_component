# -*- coding: utf-8 -*-
input_file=./简体/集藏
output_file=output/jizang_data
vocab_file=vocab2.txt


python create_pretraining_data.py \
--input_file ${input_file} \
--output_file ${output_file} \
--vocab_file ${vocab_file} \
--do_whole_word_mask True