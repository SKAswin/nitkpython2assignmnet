# problem 1
# list_1=[1,2,3,10]
# y=list_1.copy()
# var=int
# for i in range(0,len(list_1)):
#     k=list_1[i]
#     # print(k)
#     y.remove(k)
#     # print(y)
#     for j in y:
#         # print(k)
#         # print(j)
#         if k==j:
#             var=1
#
# if var==1:
#     print("false")
# else:
#     print("true")

# list_1=[5,4,3,2,1]
# y=list_1.copy()
# var=int
# for i in range(0,len(list_1)):
#     k=list_1[i]
#     # print(k)
#     y.remove(k)
#     # print(y)
#     for j in y:
#         # print(k)
#         # print(j)
#         if k==j:
#             var=1
#
# if var==1:
#     print("false")
# else:
#     print("true")

# problem 2
# list_1= [1,2,3,3,1,2,10]
# set_1=set(list_1)
# if len(set_1)!=len(list_1):
#     print("false")
# else:
#     print("true")

# list_1=[5,4,3,2,1]
# set_1=set(list_1)
# if len(set_1)!=len(list_1):
#     print("false")
# else:
#     print("true")

#problem 3
# def Remove(x):
#     y= []
#     for num in x:
#         if num not in y:
#             y.append(num)
#     return y
# x=[1,2,3,3,1,2,10]
# print(Remove(x))
# x=[1,2,1,2,1,2,1,2,1]
# print(Remove(x))

# problem4
# set_1={1,2,3}
# set_2={1,2,3,4,5}
# set_3=set_2 & set_1
# print(set_3)
# if len(set_3)==len(set_1):
#     print("true")
# else:
#     print("false")
#
# set_1={5,8,1}
# set_2={7,5,6,1,4}
# set_3=set_2 & set_1
# print(set_3)
#
# if len(set_3)==len(set_1):
#     print("true")
# else:
#     print("false")

# problrm 5
# tuple_1=(1,2,3)
# tuple_2=(4,5,6)
# list_1=[]
# for i in range(0,len(tuple_1)):
#         x=tuple_2[i]+tuple_1[i]
#         # print(x)
#         list_1.append(x)
# tuple_3=tuple(list_1)
# print(tuple_3)

# tuple_1=(9,8,7,6)
# tuple_2=(1,1)
# list_1=[]
# for i in range(0,len(tuple_2)):
#         x=tuple_2[i]+tuple_1[i]
#         # print(x)
#         list_1.append(x)
# for j in range(2,len(tuple_1)):
#     y=tuple_1[j]
#     # print(y)
#     list_1.append(y)
# tuple_3=tuple(list_1)
# print(tuple_3)

# problem 6
# tuple_1=(3,2,1)
# list_1=list(tuple_1)
# for i in list_1:
#     print(i,end="")
# print()
# tuple_1=(25,2,10)
# list_1=list(tuple_1)
# for i in list_1:
#     print(i,end="")

