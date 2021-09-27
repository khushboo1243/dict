# a={}
# num=int(input("enter the number:"))
# for i in num:
#     a.update[num]
# print(a)
# num1=int(input("enter the number:"))
# num=[1,2,3,4,5,6,7,8,9]
# num1=int(input("enter the number"))
# i=0
# k=[]
# while i<=len(num)-num1:
#     # num1=int(input("enter the number"))
#     k.append(num[-i])
#     i=i+1
# j=0
# while j<num1:
#     k.append(num[-j])
#     j=j+1
# print(k)    


# num=input("enter the number:")
# num1=int(input("enter the number:"))
# d={}
# for i in num:
#     for i in num1:

num1=int(input("enter the number:"))
num=[1,2,3,4,5,6,7,8,9]
i=0
k=[]
while i<len(num)-num1:
    k.append(num[i])
    i=i+1
print(k)
j=1
while j<=num1:
    k.append(num[-j])
    j=j+1
print(k)        