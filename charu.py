# 插入排序
def charu(array):
    for i in range(1,len(array)):
        num=array[i]
        j=i
        while array[j-1]>num and j >0:
            array[j]=array[j-1] #将前面的数值赋值给后面的
            j-=1
        array[j]=num #使用num使其回到正确的位置
    return array

if __name__ == '__main__':
    a=[23,6,7,1,2,3,3,55]
    print(charu(a))

