#!/usr/bin/env python
# coding: utf-8

# # Recursion

# # Sum of digits of positive integer number using recursive

# In[9]:


def sumOfDigit(n):
    assert n >= 0 and int(n) == n , "Sum Of Number must be positive integer only"
    if n in [0]:
        return n
    else :
        return n % 10 + sumOfDigit(n//10)
print(sumOfDigit(89))


# # Calculate power of a number using recursion

# In[2]:


def power(x,n):
    assert type(x) == int and x >= 0, "X must be a positive integer"
    assert type(n) == int and n >= 0, "N must be a non-negative integer"
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
print(power(4,4))


# # GCD (Greatest Common Divisor) of two number using recursion

# In[33]:


def gcd(a, b):
    assert isinstance(a, int) and a >= 0, "a must be a positive integer"
    assert isinstance(b, int) and b >= 0, "b must be a positive integer"
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(99,66))


# # Convert a number from decimal to binary using recursion

# In[34]:


def decimalToBinary(n):
    assert isinstance(n, int) and n >= 0, "n must be a non-negative integer"
    
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * decimalToBinary(n // 2)
print(decimalToBinary(300))


# #  Big O Notation 

# # Interview Question 1

# In[1]:


def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print("Sum = "+str(sum)+", Product = "+str(product))

ar1 = [1,2,3,4]
foo(ar1)


# # Interview Question 2

# In[2]:


def printPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))


# # Interview Question 3

# In[3]:


def printUnorderedPairs(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            print(array[i] + "," + array[j])


# # Interview Question 4

# In[4]:


def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

arrayA = [1,2,3,4,5]
arrayB = [2,6,7,8]


# # Interview Question 5

# In[6]:


def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))

print(printUnorderedPairs(arrayA,arrayB))


# # Interview Question 6

# In[7]:


def reverse(array):
    for i in range(0,int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

reverse(arrayA)


# # Interview Question 8

# In[8]:


def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))


# # Interview Question 9

# In[9]:


def allFib(n):
    for i in range(n):
        print(str(i)+":, " + str(fib(i)))

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


allFib(4)


# # Interview Question 10

# In[10]:


def powersOf2(n):
    # print("n:"+str(n))
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powersOf2(int(n/2))
        # print("prev:"+str(prev))
        print(prev)
        curr = prev*2
        print(curr)
        return curr

powersOf2(50)

