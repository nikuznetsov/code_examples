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
    