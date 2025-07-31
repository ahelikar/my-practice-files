arr=[1,20,30,40,50]
ele=25
print("Array before insertion of element")
for i in range(len(arr)):
  print(arr[i],end=" ")
  arr.insert(5,ele)
print("/n Array after insertion of element")
for i in range(len(arr)):
  print(arr[i],end=' ')

