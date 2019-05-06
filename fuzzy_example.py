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
     #name1 = 'food organic'
     #chat_text = name1.split()
     #spell_correct = [spell(i) for i in chat_text]
     #a = ' '.join(spell_correct)
     #keywords = ['search', 'want', 'show', 'open','need','buy']
     #stop_words = set(stopwords.words('english'))
     #stop_words.update(keywords)
     #filtered_sentence = [w for w in spell_correct if not w in stop_words]
     #print("inp_tf_idf", filtered_sentence)
     return fuzz.token_set_ratio(name, a)
  a = inp
  #df = df[df.apply(get_ratio, axis=1) > 75]
  df = df_product[df_product.apply(get_ratio, axis=1) > 75]
  #print(spell("darjeelling teea"))
  match_list= df['pro_name'].tolist()
  match_list = [ i.replace('\xa0', '') for i in match_list]
  print("pro_list_example", match_list)
  tfidf_out = '&&'.join(match_list)
  print("aaaa:",tfidf_out)
  return tfidf_out
