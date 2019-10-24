import gensim
import pandas as pd
from gensim.models import KeyedVectors


model = KeyedVectors.load_word2vec_format("nkjp+wiki-forms-all-300-skipg-ns.txt")


model.wmdistance("AGD Lodówki i zamrażarki Lodówki z zamrażalnikiem", "AGD Lodówki i zamrażarki Lodówki")
#0.7890250358051902

model.wmdistance("AGD Lodówki i zamrażarki Lodówki z zamrażalnikiem", "AGD Kuchenki Mikrofalowe")
#2.246459659948586



model.wmdistance("AGD Lodówki i zamrażarki Lodówki z zamrażalnikiem", "AGD Lodówki i zamrażarki Lodówki turystyczne")
#1.1760916959489012


model.wmdistance("AGD Lodówki i zamrażarki Lodówki z zamrażalnikiem", "SDKJHBDFGKLUDRGBKLJDJFBGLBJH")
#4.176374081454891


model.wmdistance("AGD Lodówki i zamrażarki Lodówki z zamrażalnikiem", "1432874568796452")
#4.363080851045773



model.wmdistance("AGD Lodówki i zamrażarki Lodówki z zamrażalnikiem", "AGD Lodówki i zamrażarki Lodówki do zabudowy")
#1.1486862892547698


