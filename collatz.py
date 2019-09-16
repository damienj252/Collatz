import numpy
#Wrapped input function as an int 
#input - String 
n = int(input("Enter a positive integer: "))
#The number we will preform the collatz operation 


#Keep looping until we reach 1
#Note: this assumes the collatz conjecture is true
while n != 1:
    #Print the current value of N 
    print(n)

    #Check the current value of n - if even divide by 2 
    # divide n by the number on the right give me the remainder - check if even or odd
    if n % 2 == 0: 
        #Normal division = /
        #Double division = // - no decimal point
        n = n // 2

    else:
         #If n is odd - multiply by 3 and add 1
        n = (3 * n) + 1

#Finally print the 1 
print(n)
