# Create You own built-in class method
# Write a Python class to implement pow(x, n)


class power_of_variable:
   def power(self, x, n):
        if n==0:
            return 1
        
        elif x==0 and n<0:
            return

        elif n<1:
            output = (1/x)** -n
            return output

        else:
            output = x**n
            return output
            
x=int(input("Please provide an input:"))
n=int(input("Please provide the nth power value:"))
print(f"The output for {n}th power of {x} is :",power_of_variable().power(x,n))