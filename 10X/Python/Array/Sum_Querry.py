'''
Sum query
Given an array of N numbers and q queries are provided each query has a starting index and an ending 
index find the sum [L, R]. find sum of elements from [L ... R]. Note array indexing starts from 1.

Input
First Line N and Q number of queries (N <= 1e5 and Q <= 1e5).

Then a line of N elements of array

Then of Q lines each line has L and R

Output
Print the sum corresponding to each query

Example
Input:

4 2

1 2 3 4

1 2

3 4

Output:

3

7

'''
'''
n,tc=map(int,input().split())
a=[int(x) for x in input().split()]
for k in range(tc):
    b=[]
    sp,ep=map(int,input().split())
    b=a[sp-1:ep]
    print(sum(b))
'''
n,tc=map(int,input().split())
a=[int(x) for x in input().split()]
for k in range(tc):
    b=[]
    sp,ep=map(int,input().split())
    b=a[sp-1:ep]
    print(sum(b))