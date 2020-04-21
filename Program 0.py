'''
RuCode-2020

Let's call a safe string consisting of lowercase Latin letters and spaces, in which between 
any two letters contain at least two spaces. You are given a string, check whether it is secure.

standard input: s  o  c  i  a  l  d  i  s  t  a  n  c  i  n  g
standard output:safe

standard input: virus
standard output: unsafe
'''

s = input()
lst = []
flag = True
if len(s) <= 256:
    for i in range(len(s)):
        if s[i] != ' ':
            lst.append(i)
for i in range(1, len(lst)):
    if ( int(lst[i]) - int(lst[i-1]) ) < 3:
        flag = False
        break
if flag == True:
    print('safe')
else:
    print('unsafe')
    
