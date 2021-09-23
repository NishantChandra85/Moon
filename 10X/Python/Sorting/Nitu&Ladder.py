'''
Nitu & Ladder
Nitu is a civil engineer. She wants to make the paper design of the ladder, by writting a program. She already know the number of steps in the ladder n.

For example, this is the ladder of size n = 4:

   #
  ##
 ###
####
Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.

Input Format
A single integer, n, denoting the size of the staircase.

Constraints
0 < n ≤ 100
Output Format
Print a staircase of size n using # symbols and spaces.

Note: The last line must have 0 spaces in it.

Sample Input
6
Sample Output
     #
    ##
   ###
  ####
 #####
######
Explanation
The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of n = 6.

'''
n=int(input())
n=n+1
i=n-1
j=0
while i>=0 and j<=n:
    print(" "*i+"#"*j)
    i-=1
    j+=1