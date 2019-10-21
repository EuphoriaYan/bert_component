# -*- coding: utf-8 -*-
config_path=configs/bert_config.json
input_file=output/pretraining_data
output_dir=output/


python run_pretraining.py \
--bert_config_file ${config_path} \
--input_file ${input_file} \
--output_dir ${output_dir} \
--do_train True \
--do_eval True