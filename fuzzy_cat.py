import pandas as pd
from fuzzywuzzy import fuzz
from autocorrect import spell 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
df_parent = pd.read_csv('parent.csv')

df_product = pd.read_csv('AR_Data_Product.csv')
def home(inp):
   def get_ratio(row):
     name = row['category_name']
     #name1 = 'soaps'
     #chat_text = name1.split()
     #spell_correct = [spell(i) for i in chat_text]
     #a = ' '.join(spell_correct)
     #keywords = ['search', 'want', 'show', 'open','need','buy']
     #stop_words = set(stopwords.words('english'))
     #stop_words.update(keywords)
     #filtered_sentence = [w for w in spell_correct if not w in stop_words]
     #print("inp_tf_idf", filtered_sentence)
     return fuzz.token_set_ratio(name, name1)
   name1 = inp
   #df = df[df.apply(get_ratio, axis=1) > 75]
   df = df_parent[df_parent.apply(get_ratio, axis=1) > 75]
   match_list= df['category_name'].tolist()
   #return match_list
   tfidf_out = '&'.join(match_list)
   tfidf_out = "tfidf"+tfidf_out
   return tfidf_out
