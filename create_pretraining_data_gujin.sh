# -*- coding: utf-8 -*-
input_file=corpus/cleaned/gujin.txt
output_file=tfrecords/gujin.tfrecord1,tfrecords/gujin.tfrecord2,tfrecords/gujin.tfrecord3,tfrecords/gujin.tfrecord4
vocab_file=vocab2.txt


python create_pretraining_data.py \
--input_file ${input_file} \
--output_file ${output_file} \
--vocab_file ${vocab_file} \
--do_whole_word_mask True
