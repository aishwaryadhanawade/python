# lst = [1, 2, 3, 4, 5, 1, 3, 2, 5, 2, 1, 4, 2, 1, 2]
#
# dicty = zip(lst, lst)
# dct = dict(dicty)
# for i in lst:
#     c = lst.count(i)
#     dct.update({i: c})
# print(dct)
#
# for a in dct.values():
#     if a > 2:
#
#         for i in dct:
#             if dct[i] == a:
#                 break
#             print(i)
import re
from array import *
from numpy import *

#
# arr = array('i', [])
#
# n = int(input("Enter the size of array:"))
#
# for i in range(n):
#     e = int(input("Enter the elements of array:"))
#     arr.append(e)
#
# print(arr)
#
# s = int(input("Enter the element that want to search:"))
#
# c = 0
# for i in arr:
#     # print(i)
#     if i == s:
#         print(c)

# c += 1


# names = []
# n = int(input("Enter the number of names want to add: "))
# for i in range(n):
#     nm = input("Enter the names want to add: ")
#     names.append(nm)
# print(names)
#
# for i in names:
#     if len(i) > 5:
#         print(i)


# a = 0
# b = 1
# n = int(input("Enter the number:"))
# if n <= 0:
#     print("invalid")
# elif n == 1:
#     print(a)
# else:
#     print(a, b)
#     for i in range(2, n):
#         c = a + b
#         a = b
#         b = c
#
#         if c >=99:
#             break
#         print(c)


# linear search
# l = [1, 2, 4, 6, 3, 9]
# n = int(input("enter the element you want to search:"))
#
#
# def search(l, n):
#     for i in l:
#         if i == n:
#             return True
#
#
# if search(l, n):
#     print("found")
# else:
#     print("not found")


# binary search
# def search(list,n):
#
#     lb = 0
#     ub = len(l) - 1
#
#     while lb <= ub:
#         mid = (lb + ub) // 2
#         if l[mid] == k:
#             return True
#         else:
#             if l[mid] < k:
#                 lb = mid+1
#             else:
#                 ub = mid-1
#     return False
# l = [1, 2, 4, 6, 9]
# k = 10
#
# if search(list,k):
#     print("found")
# else:
#     print("not found")


# bubble sort
# def sort(l):
#     for i in range(len(l) - 1, 0, -1):
#         for j in range(i):
#             if l[j] > l[j + 1]:
#                 temp = l[j]
#                 l[j] = l[j + 1]
#                 l[j + 1] = temp
#
#
# l = [2, 8, 6, 7, 3, 4, 5]
# sort(l)
# print(l)


# selection sort
# def sort(l):
#     for i in range(len(l)):
#         minv = i
#
#         for j in range(i, len(l)):
#             if l[j] < l[minv]:
#                 minv = j
#
#         temp = l[i]
#         l[i] = l[minv]
#         l[minv] = temp
#
#
# l = [9, 3, 7, 2, 4, 8, 1]
# sort(l)
# print(l)


# l = [a for a in range(1, 1001) if a % 8 == 0]
# print(l)
#


# ll = ["sumeet", "sd", "sd"]
# x = set((i, ll.count(i)) for i in ll)
# print(x)


# ll="sumeet"
# for a in ll:
#     print(a)
# sDict = {a: ll.count(a) for a in ll} #d={key:value}
# print(sDict)


# import re
# l = [1, 'a', '@']

# s = ''.join(str(x) for x in l)
# m = re.findall(r'\d', s)
# s1 = re.findall(r'[a-z]|[A-Z]', s)
# s2=re.findall(r'[^a-zA-Z0-9]',s)
# print(m, s1,s2)

#
# ll = []
# l1 = []
#
# for i in l:
#     if type(i) == int:
#         ll.append(i)
#     else:
#         l1.append(i)
# print(ll, l1)

#
# for i ,j in enumerate(l):
#     print(i,j)
#
# dic=dict(enumerate(l))
# print(dic)
# l=[i for i in range(1,1001) if i%8==0]
# for i in range (5):
#     l.append(i)

# print(l)


# l2=[(i,j) for i,j in enumerate(l)]
# print(l2)


# class Student:
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b
#
#     def __add__(self, other):
#         m1 = self.x + self.y
#         m2 = other.x + other.y
#         s3 = Student(m1, m2)
#         return s3
#
#
# s1 = Student(2, 3)
# s2 = Student(2, 4)
# s3 = s1 + s2

# print(s3.x)


#
# cb=(3,5,4)
#
# for i in range(10):
#     for j in range(10):
#         for p in range(10):
#             if (i,j,p)==cb:
#                 print(i,j,p,"found")
#                 exit()


# from multiprocessing import Pool
#
#
# def job(num):
#     return num * num
#
#
# if __name__ == '__main__':
#     p = Pool(processes=60)
#     data = p.map(job, range(10))
#     print(data)


# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'this is {self.name}'
#
#
# b = A('a')
# print(b)

#
# from time import sleep
# from threading import *
#
#
# class Hello(Thread):
#     def run(self):
#         for i in range(5):
#             print("Python is good!")
#             sleep(1)


# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("You're doing good!")
#             sleep(1)
#
#
# t1 = Hello()
# t2 = Hi()
#
# t1.start()
# sleep(0.2)
# t2.start()
# t1.join()
# t2.join()
# print("BUT!! UI is great, you should try it :)")


# a={'a','b',2,5,1}
# b={3,1,'b','c'}
#
# print(a.difference(b))


# class A:
#     def fadd(self, a, b):
#         return a + b
#
#
# a1 = A()
# d = a1.fadd(2, 3)
# print(d)
