# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:14:10 2021

@author: My Lenovo
"""

import pickle

training_spam_docs, training_doc_tokens, training_labels, test_labels, test_spam_docs, raw_test_clean, raw_training_clean = pickle.load(open("spam_data.p", "rb"))

training_docs = [doc[1] for doc in raw_training_clean]
test_docs = [doc[1] for doc in raw_test_clean]