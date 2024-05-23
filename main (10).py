r,c=int(input()),int(input())
l,s=[],0
for i in range(r):
  l.append(list(map(int,input().split())))
for i in l:
  print(i)
  s+=sum(i)
print("sum:",s)