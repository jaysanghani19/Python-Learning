def count(a):
    if(a==0):
        return 0
    
    count=0
    while(a>9):
        a//=10
        count+=1

    return count

def reverse_num(a):
    reverse =0
    while a != 0:
        reverse = (reverse*10) + (a%10)
        a//=10
    return reverse

def is_palindrome(num):
    reverse = reverse_num(num)
    return reverse==num

# Armstrong number is a number where the orginal num == sum of digits power to the number of digits in original num

def is_armstrong(num):
    original_num = num
    sum=0
    length = len(str(num))
    while num!=0:
        digit = num%10
        num//=10
        sum += digit ** length
    
    return sum==original_num

def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

print(count(243))
print(reverse_num(235))
print(is_palindrome(121))
print(is_palindrome(253))
print(is_armstrong(153))
print(is_prime(6))

# print(3 ** 3)