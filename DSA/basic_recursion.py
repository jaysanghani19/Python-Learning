def print_n_times_something(n):
    if(n==0):
        return
    print("Something")
    print_n_times_something(n-1)

def print_1_to_n(n):
    if(n==0):
        return
    print_1_to_n(n-1)
    print(n)

def print_n_to_1(n):
    if(n==0):
        return
    print(n)
    print_n_to_1(n-1)

def sum_of_n(n):
    if(n==0):
        return 0
    return n+sum_of_n(n-1)

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

def fibbonaci_term(n):
    if n==1 or n==2:
        return 1
    return fibbonaci_term(n-1)+fibbonaci_term(n-2)

def reverse_array(arr,start,end):
    if start >= end:
        return
    temp = arr[start]
    arr[start]=arr[end]
    arr[end]=temp
    
    reverse_array(arr,start+1,end-1)

def reverse_string(x):
    return x[::-1]
def is_palindrome(str):
    x=reverse_string(str)
    return str==x


# print_n_times_something(5)
# print("")
# print_1_to_n(5)
# print("")
# print_n_to_1(5)
# print(sum_of_n(5))
# print(fibbonaci_term(5))
# print(factorial(5))
# arr=[1,2,3,4,5]
# reverse_array(arr,0,len(arr)-1)
# print(arr)
print(is_palindrome("ABA"))
print(reverse_string("abc"))