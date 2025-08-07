%{ a=[1 3 5];
b=[2 3 6];
disp(union(a,b))
disp("Hello matlab")
sum=0;
for i=1:100;
    sum=sum+i;
end
disp(sum)%}


function f = fibonacci_recursive(n)
    if n == 1 || n == 2
        f = 1;
    else
        f = fibonacci_recursive(n-1) + fibonacci_recursive(n-2);
    end
end

n = 10; % Number of Fibonacci numbers
fibonacci = arrayfun(@fibonacci_recursive, 1:n);
disp(fibonacci);

