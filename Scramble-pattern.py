a=int(input("Enter the no of terms you want to eneter")
for i in range(1,a):
   for j in range(1,i):
     if i>j or i==j:
       print("*")
     elif i%j==0:
       print("#")
     else:
        print(" ")
   print()
