#!/bin/sh

vocab="data/vocab.json"
train_src="data2/train_ch.txt"
train_tgt="data2/train_en.txt"
dev_src="data2/val_ch.txt"
dev_tgt="data2/val_en.txt"
test_src="data2/test_ch.txt"
test_tgt="data2/test_en.txt"

work_dir="work_dir"

mkdir -p ${work_dir}
echo save results to ${work_dir}

training
python nmt.py \
    train \
    --cuda \
    --vocab ${vocab} \
    --train-src ${train_src} \
    --train-tgt ${train_tgt} \
    --dev-src ${dev_src} \
    --dev-tgt ${dev_tgt} \
    --input-feed \
    --valid-niter 750 \
    --batch-size 64 \
    --hidden-size 256 \
    --embed-size 256 \
    --uniform-init 0.1 \
    --label-smoothing 0.1 \
    --dropout 0.2 \
    --clip-grad 5.0 \
    --max-epoch 300 \
    --save-to ${work_dir}/model.bin \
    --lr-decay 0.5 \
    --weight-decay 0.001

# decoding
python nmt.py \
    decode \
    --cuda \
    --beam-size 5 \
    --max-decoding-time-step 100 \
    ${work_dir}/model.bin \
    ${test_src} \
    ${work_dir}/decode.txt

perl multi-bleu.perl ${test_tgt} < ${work_dir}/decode.txt
