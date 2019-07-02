chater=int(input())
valu=list(map(int,input().split()[:chater]))
valu.sort()
for i in valu:
  print(i,end=" ")
