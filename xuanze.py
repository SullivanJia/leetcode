# 选择排序
def xuanze (array):
    for i in range(0,len(array)):
        j=i
        key=i
        while j<len(array) :
            if array[j]<array[key]:
                key=j
            j+=1
        temp=array[i]
        array[i]=array[key]
        array[key]=temp
    return array

if __name__ == '__main__':
    a =[6,3,1,2,5,4]
    print(xuanze(a))

