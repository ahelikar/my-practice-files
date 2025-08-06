l=[1,2,3,5,'a',10]
old_val='a'
new_val='p'
for i in range(len(l)):
  if l[i]==old_val:
    l[i]=new_val
print(l)
