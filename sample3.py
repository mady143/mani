
# from sklearn.feature_extraction.text import TfidfVectorizer
# from ngram import NGram
# import ngram




# df_dirty = {"name":["gogle","bing","amazn","facebook","fcbook","abbasasdfzz","zsdfzl"]}

# df_clean = {"name":["google","bing","amazon","facebook"]}

# print (df_dirty["name"])
# print (df_clean["name"])

# vectorizer = TfidfVectorizer(min_df=1, analyzer=ngrams)
# print(vectorizer)
# tf_idf_matrix_clean = vectorizer.fit_transform(df_clean['name'])
# tf_idf_matrix_dirty = vectorizer.transform(df_dirty['name'])

# t1 = time.time()
# matches = awesome_cossim_top(tf_idf_matrix_dirty, tf_idf_matrix_clean.transpose(), 1, 0)
# t = time.time()-t1
# print("SELFTIMED:", t)

# matches_df = get_matches_df(matches, df_dirty['name'], df_clean['name'], top=0)

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(matches_df)


