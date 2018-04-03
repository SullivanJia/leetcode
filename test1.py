def  add(a):
    array.append(a)


def  delete(a):
    array.pop(a)


def  juge(a):
    print(array)

def option(a,str):
    print(" =========="+str(a))
    if a>3:
        if str[0] == 1:
           add(str[1])
           bian=a+1
        else:
            delete(str[1])
            bian=a-1
    else:
        if a<=2:
            print("NO")
            if int(str[0])==1:
                bian = a+1
                print(bian)
            else:
                bian=a-1
        else:
            if str[0]==1:
                bian=a+1
            juge(str[1])

if __name__ == '__main__':
    num=int(input())
    d=dict()
    array = list() #将边长存放
    bian = 0
    for i in range(0,num) :
        print(bian)
        d[i]=input()
        option(bian,d[i].split(' '))
    # str = '1 1'
    # print((str.split(' ')))


    # option(bian)




