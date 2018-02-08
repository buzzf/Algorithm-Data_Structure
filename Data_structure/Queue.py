# Python实现

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# q = Queue()
# print(q.isEmpty())
# q.enqueue('A')
# q.enqueue(34)
# q.enqueue(True)
# print(q.size())
# print(q.dequeue())
# print(q.size())
# print(q.dequeue())
# print(q.dequeue())
# print(q.size())

# 应用一：烫手山芋，约瑟夫问题

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()
    return simqueue.dequeue()

# print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

# 应用二：模拟打印机

# 在计算机科学实验室里考虑下面的情况。平均每天大约10名学生在任何给定时间在实验室工作。这些学生通常在此期间打印两次，这些任务的长度范围从1到20页。实验室中的打印机较旧，每分钟以草稿质量可以处理10页。打印机可以切换以提供更好的质量，但是它将每分钟只能处理五页。较慢的打印速度可能会使学生等待太久。应使用什么页面速率？
# 我们可以通过建立一个模拟实验来决定。我们将需要为学生，打印任务和打印机构建表现表示（Figure 4）。当学生提交打印任务时，我们将把他们添加到等待列表中，一个打印任务的队列。 当打印机完成任务时，它将检查队列，以检查是否有剩余的任务要处理。我们感兴趣的是学生等待他们的论文打印的平均时间。这等于任务在队列中等待的平均时间量。 

# 为了为这种情况建模，我们需要使用一些概率。例如，学生可以打印长度从 1 到 20 页的纸张。如果实验室中有 10 个学生，每人打印两次，则平均每小时有 20 个打印任务，意味着平均每 180 秒将有一个任务，对于每一秒，我们可以通过生成 1 到 180 之间的随机数来模拟打印任务发生的机会。

# Printer 类（Listing 2）需要跟踪它当前是否有任务。如果有，则它处于忙碌状态（13-17 行），并且可以从任务的页数计算所需的时间。构造函数允许初始化每分钟页面的配置，tick 方法将内部定时器递减直到打印机设置为空闲(11 行)

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

# Task 类（Listing 3）表示单个打印任务。创建任务时，随机数生成器将提供 1 到 20 页的长度。我们选择使用随机模块中的 randrange 函数。每个任务还需要保存一个时间戳用于计算等待时间。此时间戳将表示任务被创建并放置到打印机队列中的时间。可以使用 waitTime 方法来检索在打印开始之前队列中花费的时间。

import random

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

# PrintQueue 对象是我们现有队列 ADT 的一个实例。newPrintTask 决定是否创建一个新的打印任务。我们再次选择使用随机模块的 randrange 函数返回 1 到 180 之间的随机整数。打印任务每 180 秒到达一次。通过从随机整数（32 行）的范围中任意选择，我们可以模拟这个随机事件。模拟功能允许我们设置打印机的总时间和每分钟的页数。

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append(nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False
        
print('One hour, 1 minute print 5 pages:')
for i in range(10):
    simulation(3600,5)

print('One hour, 1 minute print 10 pages:')
for i in range(10):
    simulation(3600,10)

