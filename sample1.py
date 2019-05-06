from autocorrect import spell

a =input("enter the product:")
# print("strt",a) 
b = a.split()
print("b",b)
# print(type(b))

c = [spell(a) for a in b]
d = " ".join(c)
print(d)
	
main_url = 'https://www.arogyarahasya.com/catalogsearch/result/?q={}'
product_list = ['almonds', 'almond oil', 'face wash', 'honey', 'flax seed oil capsules','hair oils','utensils','soaps','cow products', 'beauty care','perfumes','green tea','ginger tea','lemon tea','masala tea']
# print("a",a)
# print(type(a))
if d in product_list:
	print("a",a)
	str2 = d.split()
	print("str1",str2)
	str2 = '+'.join(str2)
	print("str2",str2)
	url = main_url.format(str2)
	bot =url
	print(bot)

	# print("a_out",type(b))


