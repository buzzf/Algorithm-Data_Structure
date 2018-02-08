# 递归求和

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

# print(listsum([1,3,5,7,9]))


# 进制转换

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

# print(toStr(1453,16))

# 进制转换(使用栈）

from pythonds.basic.stack import Stack

rstack = Stack()

def toStr2(n,base):
	convertString = '0123456789ABCDEF'
	while n > 0:
		if n < base:
			rstack.push(convertString[n])
		else:
			rstack.push(convertString[n%base])
		n = n // base

	res = ''
	while not rstack.isEmpty():
		res = res + str(rstack.pop())
	return res

# print(toStr2(1453, 16))

import turtle

# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()

# def drawSpiral(myTurtle, lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle,lineLen-5)

# drawSpiral(myTurtle,100)
# myWin.exitonclick()

# 生成树形

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("green")
#     tree(75,t)
#     myWin.exitonclick()

# main()

#  谢尔宾斯基三角形

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

# def main():
#    myTurtle = turtle.Turtle()
#    myWin = turtle.Screen()
#    myPoints = [[-100,-50],[0,100],[100,-50]]
#    sierpinski(myPoints,3,myTurtle)
#    myWin.exitonclick()

# main()

# 汉诺塔游戏
# 方法一

def move(n, a, b, c):
    if n==1:
        print(a,'-->',c)
        return
    else:
        move(n-1,a,c,b)  #首先需要把 (N-1) 个圆盘移动到 b
        move(1,a,b,c)    #将a的最后一个圆盘移动到c
        move(n-1,b,a,c)  #再将b的(N-1)个圆盘移动到c
# move(4, 'A', 'B', 'C')

# 方法二

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

# moveTower(5, 'A', 'B', 'C')

# 硬币找零

def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

print(recDC([1,5,10,20,21,50], 63, [0]*64))
