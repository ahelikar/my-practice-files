def fibo_sum(int n):
  sum=0;
  sum+=1+((fibo_sum(n-1))+(fibo_sum(n-2))
  return sum 
if __name__==__"main"__
m=int(input("Enter the no of terms"))
print(fibo_sum(m))
