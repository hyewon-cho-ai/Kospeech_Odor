#!/bin/bash

# 데이터셋 경로와 다른 필수 변수를 설정합니다.
DATASET_PATH="C:\\Users\\User\\Desktop\\dataset_file"
VOCAB_DEST="C:\\Users\\User\\PycharmProjects\\kospeach_Project\\kospeech\\vocab_dest"
OUTPUT_UNIT='character'                                         # character / subword / grapheme
PREPROCESS_MODE='phonetic'                                      # phonetic: 칠 십 퍼센트,  spelling: 70%
VOCAB_SIZE=5000                                                 # if you use subword output unit, set vocab size

echo "Pre-process KsponSpeech Dataset.."

python main.py \
--dataset_path "$DATASET_PATH" \
--vocab_dest "$VOCAB_DEST" \
--output_unit "$OUTPUT_UNIT" \
--preprocess_mode "$PREPROCESS_MODE" \
--vocab_size "$VOCAB_SIZE"



