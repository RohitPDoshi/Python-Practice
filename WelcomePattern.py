'''Mr Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

•	Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
•	The design should have 'WELCOME' written in the center.
•	The design pattern should only use |, . and - characters.

Sample Designs

Size: 7 x 21 

---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------


    Size: 11 x 33

---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------

Input Format
A single line containing the space separated values of N and M.

Constraints
•	5 < N <101
•	15 < M < 303

Output Format
Output the design pattern.'''


nm=input().split()
n=int(nm[0])
m=int(nm[1])
d=".|."
# length till n//2
# lines [0 to n/2] (m-3-(6*i))//2
# lines [n/2 to n] 3*(i+1)
for i in range(n//2):
    for j in range((m-3-(6*i))//2):
        print("-",end="")
    print(d*(2*i+1),end="")
    for j in range((m-3-(6*i))//2):
        print("-",end="")
    print()
w=("-"*((m-7)//2))
print(w+"WELCOME"+w)
for i in range(n//2):
    for j in range(3*(i+1)):
        print("-",end="")
    print(d*(2*(n//2-i)-1),end="")
    for j in range(3*(i+1)):
        print("-",end="")
    print()



