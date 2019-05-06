import urllib3
import csv
import sys 
import pandas as pd 
import json 
import inflect
import pprint
import numpy as np

class dataToCSV:
	
	def init(self,*args):
		f=inflect.engine() 


		http = urllib3.PoolManager()
		#r1 = http.request('GET', 'http://magento.arogyarahasya.com/productviewcount/index/index')
		r1 = http.request('GET', 'https://magento.arogyarahasya.com/recommendation/index/api?type=category_product')
		r2 = http.request('GET', 'https://magento.arogyarahasya.com/recommendation/index/api?type=order_item')
		r3 = http.request('GET', 'https://magento.arogyarahasya.com/recommendation/index/api?type=product')
		#r4 = http.request('GET', 'https://magento.arogyarahasya.com/recommendation/index/api?type=product_view')
		r5 = http.request('GET', 'https://magento.arogyarahasya.com/recommendation/index/api?type=product_review')
		r6 = http.request('GET', 'https://magento.arogyarahasya.com/recommendation/index/api?type=product_view')
		# f.write(r1.data)

		# reload(sys)
		# sys.setdefaultencoding('utf8')
		rows = json.loads(r1.data)
		df = pd.DataFrame(rows)
		rows_sold = json.loads(r2.data)
		df_sold = pd.DataFrame(rows_sold)
		rows_data = json.loads(r3.data)
		df_data = pd.DataFrame(rows_data)
		rows_trending = json.loads(r6.data)
		df_trending = pd.DataFrame(rows_trending)
		rows_ratings = json.loads(r5.data)
		df_rating = pd.DataFrame(rows_ratings)

		df.to_csv("AR_Data1.csv", index=False, encoding='utf-8')
		df_data.to_csv("AR_Data_Cats.csv", index=False,encoding='utf-8')
		
		ids_list = df['product_id'].tolist()

		

		dfs1 = pd.DataFrame()
		dfs1["id"] = ids_list 
		dfs1 = df_sold.groupby(['product_id']).size().reset_index(name='sold')
		dfs1.to_csv("AR_Data_Sold1.csv", index=False, encoding='utf-8')
		

		dfr1 = pd.DataFrame()
		dfr1["Entity_Pk_Value"] = df_rating["entity_pk_value"] .tolist()
		dfr1["Ratings"] = df_rating["rating_summary"] .tolist()
		dfr1.to_csv("AR_Data_Ratings1.csv", index=False, encoding='utf-8')

		dfl1 = pd.DataFrame()
		dfl1["id"] = df_data['id'].tolist()
		dfl1["created_at"] = df_data["created_at"] .tolist()
		dfl1.to_csv("AR_Data_Latest.csv",index=False,encoding='utf-8')

		dft1 = pd.DataFrame()
		dft1["product_id"] = df_trending["product_id"].tolist()
		s = df_trending['product_id'].value_counts().rename('views')
		dft1 = dft1.join(s, on='product_id')
		dft1["added_at"] = df_trending["added_at"].tolist()
		dft1 = dft1.join(dfl1["created_at"])
		dft1.to_csv("AR_Data_Trending.csv", index=False, encoding='utf-8')
		

		# dfd = pd.DataFrame()
		# dfd["id"]   = df_data["id"].tolist()
		df_data["price"]=df_data["price"].astype(float)
		df_data['final_price']=df_data['final_price'].astype(float)
		df_data['Discount'] = ((df_data["price"]-df_data['final_price']) / df_data["price"]) *100

		df_data.to_csv("AR_Data_Cats.csv",index=False,encoding='utf-8',)
		#df_views.to_csv("AR_Data_views.csv",index=False,encoding = 'utf-8')

dataToCSV().init()




