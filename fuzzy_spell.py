import pandas as pd
from fuzzywuzzy import fuzz
from autocorrect import spell 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
df_parent = pd.read_csv('parent.csv')

df_product = pd.read_csv('AR_Data_Product.csv')
def home(inp):
  def get_ratio(row):
     name = row['pro_name']
     return fuzz.token_set_ratio(name, a)
  a = inp
  df = df_product[df_product.apply(get_ratio, axis=1) > 75]
  match_list= df['pro_name'].tolist()
  print("fuzzy_spell",match_list)
  match_list = [i.replace('\xa0', '') for i in match_list]
  #tfidf_out = '&'.join(match_list)
  #tfidf_out = "&"+tfidf_out
  return match_list

