#!/bin/sh

vocab="data/vocab.json"
train_src="data2/train_ch.txt"
train_tgt="data2/train_en.txt"
dev_src="data2/val_ch.txt"
dev_tgt="data2/val_en.txt"
test_src="data2/test_ch.txt"
test_tgt="data2/test_en.txt"

work_dir="work_dir"

perl multi-bleu.perl ${test_tgt} < ${work_dir}/decode.txt