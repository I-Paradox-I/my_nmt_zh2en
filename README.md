## A Basic PyTorch Implementation of Attentional Neural Machine Translation

This is a basic implementation of attentional neural machine translation (Bahdanau et al., 2015, Luong et al., 2015) in Pytorch.
It implements the model described in [Luong et al., 2015](https://arxiv.org/abs/1508.04025), and supports label smoothing, beam-search decoding and random sampling.
With 256-dimensional LSTM hidden size, it achieves 7.4 BLEU score on the 10000 size Chinese-English dataset.

### File Structure

* `nmt.py`: contains the neural machine translation model and training/testing code.
* `vocab.py`: a script that extracts vocabulary from training data
* `util.py`: contains utility/helper functions

### Environment

The code is written in Python 3.6 using some supporting third-party libraries. We provided a conda environment to install Python 3.6 with required libraries. Simply run

```bash
conda env create -f environment.yml
```

### Usage

Each runnable script (`nmt.py`, `vocab.py`) is annotated using `dotopt`.
Please refer to the source file for complete usage.

First, we extract a vocabulary file from the training data using the command:

```bash
# python vocab.py \
#     --train-src=data/train.de-en.de.wmixerprep \
#     --train-tgt=data/train.de-en.en.wmixerprep \
#     data/vocab.json

python vocab.py \
    --train-src=data2/train_ch.txt \
    --train-tgt=data2/train_en.txt \
    data/vocab.json
```

This generates a vocabulary file `data/vocab.json`. 
The script also has options to control the cutoff frequency and the size of generated vocabulary, which you may play with.

To start training and evaluation, simply run `scripts/train.sh`. 
After training and decoding, we call the official evaluation script `multi-bleu.perl` to compute the corpus-level BLEU score of the decoding results against the gold-standard.

### License

This work is licensed under a Creative Commons Attribution 4.0 International License.
