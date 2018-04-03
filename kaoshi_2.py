def solution():
    flag=0

    a=input().strip().split()
    num=list(map(int,a))
    for i in  range(num[1],num[0]+1):
        for j in range(num[1]+1,num[0]+1):
            if i%j>=num[1]:
                flag+=1
    return flag

if __name__ == '__main__':
    print(solution())