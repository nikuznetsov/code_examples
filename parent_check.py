# Check if class is parent or not
# Input:
# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A
# Output:
# Yes
# Yes
# Yes
# No

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: 
                  return newpath
        return None

cls = {}

n = int(input())
for i in range(n):
  s = input().split(' ')
  if s.count(':') > 0:
    s.remove(':')
  cls[s[0]] = s[1:]
print(cls)
q = int(input())
for i in range(q):
  r = input().split(' ')
  if find_path(cls, r[1], r[0]) == None:
    print('No')
  else:
    print('Yes')
