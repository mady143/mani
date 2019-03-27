import csv
import pandas as pd
import ast
import fuzzy_example
df_cat = pd.read_csv('parent.csv')
categories = df_cat['category_name'].tolist()
sub_cat = df_cat['subcat_name'].tolist()
product_csv = pd.read_csv('AR_Data_Product.csv')
pro_name = product_csv['pro_name'].tolist()
product_id = product_csv['product_id'].tolist()
main_url = 'https://www.arogyarahasya.com/catalogsearch/result/?q={}'
def spell_correct(a):
    if any(s.lower() == a.lower() for s in categories):
           print('spell_func')
           for m,n in zip(categories, sub_cat):
             if a.casefold() == m.casefold():
               subcat_list = ast.literal_eval(n)
               print("subcat_list", subcat_list)
               #if categories have empty list, check in the product csv
               if not subcat_list:
                 print("aaa", a)
                 product_list = fuzzy_example.home(a)
                 #product_list = [i  for i in pro_name if a.casefold() in i.casefold()]
                 product = [ product.replace(" ", '+') for product in product_list]
                 product = [i.strip('"') for i in product]
                 product_url = [ main_url.format(i) for i in product]
                 print('product_list', product_list)
                 #print('product', product)
                 #print("product_url", product_url)
                 if not product_url: 
                    c = a.split()
                    a = '+'.join(c)
                    bot = main_url.format(a)
                    print("notd", bot)
                 else:
                   str2 = '&&'.join(product_url)
                   bot = 'spell'+str2
                   print("else", bot)
               else:
                  b = '&'.join(subcat_list)
                  print("&", b)
                  bot = 'tfidf'+b
                  bot = bot 
               return bot
                  
               
