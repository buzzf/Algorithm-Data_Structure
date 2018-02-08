# 冒泡排序，相邻的值比较大小，大者往后排

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

# alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)

# 短冒泡排序

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               alist[i], alist[i+1] = alist[i+1], alist[i]
       passnum = passnum-1

# alist=[20,30,40,90,50,60,70,80,100,110]
# shortBubbleSort(alist)
# print(alist)

# 选择排序，遍历一次列表，找到最大值放到相应位置。

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

# alist = [54,26,93,17,77,31,44,55,20]
# selectionSort(alist)
# print(alist)

# 插入排序

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertionSort(alist)
# print(alist)


# 希尔排序（递增递减排序）

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      # print("After increments of size",sublistcount,"The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue


# 归并排序

def mergeSort(alist):
    # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    # print("Merging ",alist)

# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)

# 快速排序

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

# alist = [54,26,93,17,77,31,44,55,20]
# quickSort(alist)
# print(alist)

# 不同排序算法比较

import random
import time

alist1 = list(range(1,20000))
random.shuffle(alist1)

alist2 = list(range(1,20000))
random.shuffle(alist2)

alist3 = list(range(1,20000))
random.shuffle(alist3)

alist4 = list(range(1,20000))
random.shuffle(alist4)

alist5 = list(range(1,20000))
random.shuffle(alist5)

alist6 = list(range(1,20000))
random.shuffle(alist6)

alist7 = list(range(1,20000))
random.shuffle(alist7)

t1 = time.time()
shellSort(alist1)
t2 = time.time()
insertionSort(alist2)
t3 = time.time()
selectionSort(alist3)
t4 = time.time()
shortBubbleSort(alist4)
t5 = time.time()
bubbleSort(alist5)
t6 = time.time()
mergeSort(alist6)
t7 = time.time()
quickSort(alist7)
t8 = time.time()


print('shellsort time: ',t2-t1)
print('insertionSort time: ', t3-t2)
print('selectionSort time: ', t4-t3)
print('shortBubbleSort time: ', t5-t4)
print('bubbleSort time: ', t6-t5)
print('mergeSort time: ', t7-t6)
print('quickSort time: ', t8-t7)
