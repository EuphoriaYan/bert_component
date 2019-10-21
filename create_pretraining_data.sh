# -*- coding: utf-8 -*-
output_file=output/pretraining_data
vocab_file=vocab2.txt


python create_pretraining_data.py \
--output_file ${output_file} \
--vocab_file ${vocab_file} \
--do_whole_word_mask True