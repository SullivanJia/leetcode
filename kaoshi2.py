def solution():
    num=int(input())
    if num%2==1:
        return num-1
    for i in range(10000):
        if i%2==0 and 2*i==num:
            return i

        if  i%2==0 and 2*(i+1)==num:
            return i+1

if __name__ == '__main__':
    print(solution())
