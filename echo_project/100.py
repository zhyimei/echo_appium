#coding=utf-8
"""题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。"""
"""for i in range(1,5):
    for j in range(1,5):
        for k in  range(1,5):
            if i!=j and j!=k and i!=k:
                print i*100+j*10+k
"""
"""题目：输入三个整数x,y,z，请把这三个数由小到大输出。"""
"""l=[]
for i in range(1,4):
    x=int(raw_input("请输入:"))
    l.append(x)
l.sort()
print l"""
"""题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义："""


def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


# 输出了第10个斐波那契数列
print fib(10)
"""题目：将一个列表的数据复制到另一个列表中。

程序分析：使用列表[:]。"""
a=[1,4,66]
b=[]
b=a[:]
print b
"""题目：输出 9*9 乘法口诀表。

程序分析：分行与列考虑，共9行9列，i控制行，j控制列。"""
"""for i in range(1,10):
    print ""
    for j in range(1,i+1):
        print "%d*%d=%2d"%(j,i,i*j),
"""
import time
"""now=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
print now
time.sleep(2)
haha=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print haha"""
"""题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位"""
"""for i in range(100,1000):
    a=i/100
    b=i/10%10
    c=i%10
    if a**3+b**3+c**3==i:
        print i"""
"""利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
程序源代码："""
"""score=int(raw_input("请输入分数："))
if score >= 90:
    grade="A"
elif score >= 60:
    grade="B"
else:
    grade="C"
print grade"""
"""题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'"""
"""index=raw_input("请输入字符：")
eng=0
kong=0
num=0
other=0
for i in index:
    if i.isalpha():
        eng +=1
    elif i.isspace():
        kong +=1
    elif i.isalnum():
        num +=1
    else:
        other +=1
print "eng有%d,kong有%d,num有%d,other有%d"%(eng,kong,num,other)
"""
"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。"""
"""
a=raw_input("数值：")
n=raw_input("数量：")
sum=0
list=[]
"""



