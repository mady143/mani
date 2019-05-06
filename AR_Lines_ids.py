import tensorflow as tf
import numpy as np 
import pandas  as pd 
import os 
import random 
import re
import pprint  
import random 
import urllib3
import sys 
import json  
import shutil
# import config1 
from ast import literal_eval
import ast
class AR_lines_id:

	def init(self,*args):

		total_product_list = []
		total_category_list = []
		df=pd.read_csv("AR_Data_Category_Product.csv")
		ids_list = df['product_id'].tolist()
		
		cat_list1 = df["category_id"].tolist()
		
		list1=[]
		list2 = []
		for cat in cat_list1:
			sample_list = []
			for id1,cat1 in zip(ids_list,cat_list1):
				if str(cat) in str(cat1):
					sample_list.append(str(id1))
			list1.append(str(cat))
			list2.append(sample_list)
			list3 = []
			list4 = []
			for i,j in zip(list1,list2):
				if i not in list3 and j not in list4:
					list3.append(i)
					list4.append(j)	
		
		AR_products = open("AR_products1.txt", "w")
		AR_ids = open("AR_ids1.txt", "w")
		
		for cat_ids, products_ids, num in zip(list3,list4, range(0,10000,2)):
			products_ids = ",".join(str(v) for v in products_ids)	
			AR_products.write("L"+str("%04d"%(num))+" +++$+++ u1 +++$+++ m1 +++$+++ A +++$+++ " + str(cat_ids).strip() + "\n")
			AR_products.write("L"+str("%04d"%(num+1))+" +++$+++ u1 +++$+++ m1 +++$+++ A +++$+++ " + str(products_ids).strip() + "\n")
		last_num = num + 1

		AR_products=open("AR_products1.txt")
		contents_ids=AR_products.readlines()

		end_num=contents_ids[-1][1:5]
		end_num=int(end_num) 
		#print (end_num)
		for num in range(0,end_num+1,2):

			AR_ids.write("u1 +++$+++ u1 +++$+++ m1 +++$+++ "+str(["L"+str("%04d"%(num)),"L"+str("%04d"%(num+1))]))
			AR_ids.write("\n")
		AR_ids.close()

AR_lines_id().init()