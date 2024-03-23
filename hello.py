import copy

result = []
allresult=[]
def cal(inputlist):
    count=0
    for li in inputlist:
        if(type(li)==list):
            result.append(inputlist.index(li))
            cal(li)
        elif((type(li)!=int) & (type(li)!=list)):
            result.append(inputlist.index(li))
            a=copy.deepcopy(result)
            allresult.append(a)
            result.clear()

        if(type(li)==int):
            count=count+1
    if(count==len(inputlist)):
        result.clear()

if __name__ == '__main__':
    inputlist = [1, [1, 2], [[3, 4, {5, 6}], 7], [0, [0, [0, 0, {8, 9}]]]]
    cal(inputlist)
    print(allresult)