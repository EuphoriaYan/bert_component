# -*- coding: utf-8 -*-
input_file=corpus/cleaned/zibu.txt
output_file=tfrecords/zibu.tfrecord1,tfrecords/zibu.tfrecord2,tfrecords/zibu.tfrecord3
vocab_file=vocab2.txt


python create_pretraining_data.py \
--input_file ${input_file} \
--output_file ${output_file} \
--vocab_file ${vocab_file} \
--do_whole_word_mask True
