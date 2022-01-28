#!/usr/local/bin/python

import fasttext
import argparse
import numpy as np

def transform_sentence_file(file):
    file_clean = []
    for sentence in file:
        sentence = sentence.split(' ')[2:-1]
        file_clean.append(sentence)
    return file_clean

def vectors(lang_id, model):
    path = '../data/raw/golden_collection/sentences/1-100-final.'+str(lang_id)
    lines = open(path, 'r')
    text = transform_sentence_file(lines.readlines())
    model_name = 'cc.'+str(lang_id)+'.'+str(model)+'.bin'
    ft = fasttext.load_model(model_name)
    vectors = np.asarray([[ft.get_word_vector(text[i][j]) for j in range(len(text[i]))] for i in range(len(text))])
    np.save('../data/processed/models/vector_'+str(lang_id)+'_'+str(model), vectors)

def main():
    global args

    parser = argparse.ArgumentParser(
        description='Save fastText embeddings')
    parser.add_argument("language", type=str, default="en",
                        help="language identifier.")
    parser.add_argument("size", type=str, default="100",
                        help="dimension of the model embeddings : 100 or 300.")
    args = parser.parse_args()

    vectors(args.language, args.size)

if __name__ == '__main__':
    main()