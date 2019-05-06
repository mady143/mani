import urllib3
import csv
import sys 
import pandas as pd 
import json 
import inflect
import pprint
import numpy as np
import os.path
import csv
class dataToCSV:
	
	def init(self,*args):
		f=inflect.engine() 


		http = urllib3.PoolManager()
		#r1 = http.request('GET', 'http://magento.arogyarahasya.com/productviewcount/index/index')
		r1 = http.request('GET', 'https://magento.arogyarahasya.com/recommendation/index/api?type=category_product')
		r2 = http.request('GET', 'https://magento.arogyarahasya.com/recommendation/index/api?type=product')
		r3 = http.request('GET','https://magento.arogyarahasya.com/recommendation/index/api?type=category')

		# reload(sys)
		# sys.setdefaultencoding('utf8')
		rows = json.loads(r1.data)
		df = pd.DataFrame(rows)
		rows_product = json.loads(r2.data)
		df_product = pd.DataFrame(rows_product)
		rows_categorry = json.loads(r3.data)
		df_category = pd.DataFrame(rows_categorry)
		
		df1 = pd.DataFrame()
		df1['category_id']=df['category_id']
		df1['product_id']=df['product_id']
		df1.to_csv("AR_Data_Category_Product.csv", index=False)

		
		df_product['product_id'] = df_product['id']
		df_product['pro_name'] = df_product['name']
		#df_product['final_price'] = df_product['final_price']
		df_product = df_product.drop(['final_price','id','created_at','is_salable','price','qty','sku','website_ids','status','visibility','name'], axis=1)
		df_product.to_csv("AR_Data_Product.csv", index=False)
		# print(df_items)
		df3 = pd.DataFrame()
		df3['category_id']  = df_category['id']
		df3['category_name'] = df_category['name']
		df3['parent_id']     = df_category['parent_id']
		df3.to_csv("AR_Category.csv",index=False)


		df=pd.read_csv("AR_Data_Category_Product.csv")
		
		ids_list = df['product_id'].tolist()
		
		cat_list = df["category_id"].tolist()
		df4 = pd.DataFrame()
		df4 = df_product.merge(df1,  how='inner')
		df4 = df4.merge(df3, how = 'inner')
		#df4 = df4.drop(['final_price','id','created_at','is_salable','price','qty','sku','website_ids','status','visibility'], axis=1)
		df4.to_csv("AR_All.csv", index=False)

		data1 = pd.read_csv("AR_All.csv")
		cat_name = list(data1['category_name'])
		list1 = []
		for i in cat_name:
			if i not in list1:
				list1.append(i)
		print("list1",list1)




		lll={}
		df_cats = pd.read_csv("AR_Category.csv")
		category_list = df_cats["category_name"].tolist()
		#lllll=["Beauty Care"]
		for cat in category_list:
			df11=df_cats.loc[df_cats['category_name']==str(cat)]
			id_list=df11["category_id"].tolist()[0]
			#print(id_list)
			parent_df=df_cats.loc[df_cats["parent_id"]==int(id_list)]
			parent_names=parent_df["category_name"].tolist()
			lll[str(cat)]=parent_names

		#print(lll)
		csv_columns = ['category_name','parents_name']
		with open('AR_Parents.csv', 'w') as f:
			writer = csv.writer(f)
			writer.writerow(['category_name','parents_name'])
			for row in lll.items():
				writer.writerow(row)


dataToCSV().init()