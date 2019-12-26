# AIM: Write a recursive code to compute the nth Fibonacci number.

def fib(n):
    if n==1:                    #1st term is 0
        return 0
    elif n==2:                  #2nd term is 1
        return 1
    else:
        return fib(n-1)+fib(n-2)
#__main__
n=int(input("Enter last term required:"))
for i in range(1,n+1):
    print(fib(i),end=',')
print("...")
print(n"th","Fibonacci number is",fib(n))
