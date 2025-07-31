from collections import Counter
def get_freq(a):
  freq=Counter(a)
  return freq
my_ar=[1,2,2,2,3,3,3,4,4,4,4,4]
print(get_freq(my_ar))
for element,count in (get_freq(my_ar)).items():
   print(f"Element{element}occurs {count}times)
