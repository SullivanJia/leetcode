# 冒泡排序
def maopao(array):
    for i in range(0,len(array)):
        j=i+1
        for k in range(j,len(array)):
            if array[k]<array[i]:
                temp=array[k]
                array[k]=array[i]
                array[i]=temp
    return array
if __name__ == '__main__':
    a=[23,1,2,3,4,5,6]
    print(maopao(a))