def rotate_right(a,k):
 n=len(a)
 k=k%n
 rot_ar=a[-k:]+a[:-k]
  return rot_a
my_ar=[1,2,3,4,5]
k_pos=3
print("Array after rotation",(rotate_right(my_ar,k_pos)))
