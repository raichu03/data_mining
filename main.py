import os
import pandas as pd
import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Embedding, Bidirectional, Dense
from tensorflow.keras.layers import LSTM 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import TextVectorization


MAX_FEATURES = 200000 # number of words in the vocab

df = pd.read_csv(os.path.join('Datasets','train.csv', 'train.csv'))
X = df['comment_text']
y = df[df.columns[2:]].values

vectorizer = TextVectorization(max_tokens=MAX_FEATURES,
                               output_sequence_length=1800,
                               output_mode='int')
vectorizer.adapt(X.values)

vectorized_text = vectorizer(X.values)

import tensorflow as tf


model = tf.keras.models.load_model('Models/toxicity.h5')

input_str = vectorizer('hey i freaken hate you!')

res = model.predict(np.expand_dims(input_str,0))

res

def score_comment(comment):
    vectorized_comment = vectorizer([comment])
    results = model.predict(vectorized_comment)
    print(results)
    
    # text = ''
    # for idx, col in enumerate(df.columns[2:]):
    #     text += '{}: {} ||||||||||| '.format(col, results[0][idx]>0.5)
    
    # return text
    scores = {}
    
    # Populate the dictionary with column names and prediction results
    for idx, col in enumerate(df.columns[2:]):
        scores[col] = results[0][idx] > 0.5
    
    print(scores['toxic'])
    return scores