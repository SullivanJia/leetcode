import random
lr=1
while lr != 0:
	lr=input("下限：")
	rr=input("上限：")
	print(random.randint(int(lr),int(rr)))