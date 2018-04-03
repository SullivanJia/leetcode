def xuanze(a):
    for i in range(len(a)):
        j=i
        num=i
        while j<len(a):
            if a[j]<a[num]:
                num=j
            j+=1
        tmp=a[i]
        a[i]=a[num]
        a[num]=tmp
    return a






if __name__ == '__main__':
    a=[2,3,4,5,1,6]
    print(xuanze(a))