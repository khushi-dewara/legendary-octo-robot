#Aim: Recursively find the factorial of a natural number.

n=int(input("enter the natural number:"))
def factorial(n):
    if n==0:
        if n==0:
            return 1
        else:
            n*facttorial(n-1)
            
#_main_
print(factorial(n))
    

