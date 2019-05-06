import urllib3
import json
import sys
import pandas as pd

def csv_creation(url):
	http = urllib3.PoolManager()
		
	r1 = http.request('GET',url)
	# reload(sys)
	# sys.setdefaultencoding('utf8')
	rows = json.loads(r1.data)
	df = pd.DataFrame(rows)
	filename=url.split("type=")[1]+".csv"
	df.to_csv(filename, index=False,encoding='utf8') 



urls_list=["https://magento.arogyarahasya.com/recommendation/index/api?type=order","https://magento.arogyarahasya.com/recommendation/index/api?type=order_item","https://magento.arogyarahasya.com/recommendation/index/api?type=product_review","https://magento.arogyarahasya.com/recommendation/index/api?type=product_view","https://magento.arogyarahasya.com/recommendation/index/api?type=product","https://magento.arogyarahasya.com/recommendation/index/api?type=category","https://magento.arogyarahasya.com/recommendation/index/api?type=category_product"]

for url in urls_list:
	csv_creation(url)
 

#pradeep

dfb=pd.read_csv("product_review.csv")
df5 = pd.DataFrame()
df5['id']=dfb['entity_pk_value']
df5['rating']=dfb['rating_summary']
df5['reviews_count']=dfb['reviews_count']
dfl=pd.read_csv("product.csv")
dfl = dfl.merge(df5, on='id', how="outer").fillna(0)
dfb=pd.read_csv("product_view.csv")
dd = list(dfb['product_id'])
frequencytable = {}
for key in dd:
	if key in frequencytable:
	    frequencytable[key] += 1
	else:
	    frequencytable[key] = 1

df5 = p=pd.DataFrame()
df5['id']=frequencytable.keys()
df5['views']=frequencytable.values()
dfl = dfl.merge(df5, on='id', how="outer").fillna(0)
dfb=pd.read_csv("order_item.csv")
dd = list(dfb['product_id'])
frequencytable = {}
for key in dd:
	if key in frequencytable:
	    frequencytable[key] += 1
	else:
	    frequencytable[key] = 1

df5 = p=pd.DataFrame()
df5['id']=frequencytable.keys()
df5['sold']=frequencytable.values()
dfl = dfl.merge(df5, on='id', how="outer").fillna(0)
dfl=dfl.drop_duplicates(subset=['id'])
dfl['Discount'] = ((dfl["price"]-dfl['final_price']) / dfl["price"]) *100
dfl['Percentages'] = (dfl["sold"]/dfl['views']) *100
dfl['id']=dfl['id'].astype(int)
dfl.to_csv("AR_all1.csv", index=False)
dfb=pd.read_csv("product_view.csv")
df5 = p=pd.DataFrame()
df5['id']=dfb['product_id']
df5['added_at']=dfb['added_at']
dfl = dfl.merge(df5, on='id', how="outer").fillna(0)
dfl['views1'] = dfl.groupby('id').cumcount() + 1 
dfl['id']=dfl['id'].astype(int)
dfl.to_csv("AR_all_trend1.csv", index=False)


