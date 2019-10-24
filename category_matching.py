import gensim
import pandas as pd
from gensim.models import KeyedVectors


model = KeyedVectors.load_word2vec_format("nkjp+wiki-forms-all-300-skipg-ns.txt")


