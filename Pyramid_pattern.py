n=int(input())
for i in range(1,n+1):
  print(" "*(n-i),end=" ")
  for j in range(1,i+1):
     print(j,end=" ")
for i in range(n-1,0,-1):
  print(" "*(n-1),end=" ")
  for j in range(i,i+1):
     print(j,end=" ")
   print()

