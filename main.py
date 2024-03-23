n,q=map(int,input().split(' '))
init_num=map(int,input().split(' '))
init_num=[int(data) for data in init_num]
for i in range(q):
    l,r,c=map(int,input().split(' '))
    for j in range(l-1,r):
        init_num[j]+=c
print(init_num)