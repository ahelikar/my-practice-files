l1=[2,3,9,10]
l2=['a','p','e','o','l']
l3=['t',1,'o',11,12]
for a,b,c in itertools.zip_longest(l1,l2,l3,fill_value=' '):
 print(a,b,c)
