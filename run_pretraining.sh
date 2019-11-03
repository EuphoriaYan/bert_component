# -*- coding: utf-8 -*-
config_path=configs/bert_config.json
input_file=output/jizang_data.tfrecord,output/ruzang_data.tfrecord,output/shi1zang_data.tfrecord,output/shi3zang_data.tfrecord1,output/shi3zang_data.tfrecord2,output/shi3zang_data.tfrecord3,output/zizang_data.tfrecord
output_dir=output/


python run_pretraining.py \
--bert_config_file ${config_path} \
--input_file ${input_file} \
--output_dir ${output_dir} \
--do_train True \
--do_eval True