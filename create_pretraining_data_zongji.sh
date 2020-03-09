# -*- coding: utf-8 -*-
input_file=corpus/cleaned/zongji.txt
output_file=tfrecords/zongji.tfrecord1,tfrecords/zongji.tfrecord2,tfrecords/zongji.tfrecord3,tfrecords/zongji.tfrecord4
vocab_file=vocab2.txt


python create_pretraining_data.py \
--input_file ${input_file} \
--output_file ${output_file} \
--vocab_file ${vocab_file} \
--do_whole_word_mask True
