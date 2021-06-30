from typing import List
from functools import reduce
import numpy as np
import matplotlib.pyplot as plt
import xlwt
import matplotlib
import math

'''先引入必要的包'''
def plot(time,t,A,B):
    # -*- coding: utf-8 -*-
    import math
    import numpy as np #导入数值计算模块
    import matplotlib.pyplot as plt #导入绘图模块
    import mpl_toolkits.axisartist as axisartist #导入坐标轴加工模块
    fig=plt.figure(figsize=(6,4)) #新建画布
    ax=axisartist.Subplot(fig,111) #使用axisartist.Subplot方法创建一个绘图区对象ax
    fig.add_axes(ax) #将绘图区对象添加到画布中

    ax.axis[:].set_visible(False) #隐藏原来的实线矩形

    ax.axis["x"]=ax.new_floating_axis(0,0,axis_direction="bottom") #添加x轴
    ax.axis["y"]=ax.new_floating_axis(1,0,axis_direction="bottom") #添加y轴

    ax.axis["x"].set_axisline_style("->",size=1.5) #给x坐标轴加箭头
    ax.axis["y"].set_axisline_style("->",size=1.5) #给y坐标轴加箭头
    ax.annotate(text='x' ,xy=(3.5,0.1) ,xytext=(3.5,0.1),fontsize='x-large') #标注x轴
    ax.annotate(text='y' ,xy=(0,2.5) ,xytext=(-0.35,2.5),fontsize='x-large') #标注y轴

    plt.xlim(1,2) #设置横坐标范围
    plt.ylim(-1,1) #设置纵坐标范围
    ax.set_xticks([1,2,3]) #设置x轴刻度
    ax.set_yticks([-0.5,0,0.5]) #设置y轴刻度
    # ax.set_title('Demo Figure')
    ss='(%f,0)'%(t - A/B)
#     plt.text(t - A/B, 0, ss)

    y=[] #用来存放函数值
    x=np.linspace(-3,3,100) #构造横坐标数据
    y=x**2-2
    # for xi in x: #生成函数值
    #     y.append(math.sin(xi))#追加
    z=B*x+A-B*t
    s='y=%f*(x-%f)+%f'%(B,t,A)
    plt.plot(x,y,color="blue",label='y=x^2-2', linewidth=1) #描点连线
    plt.plot(x,z,color="red",linestyle='--', linewidth=1 ,label=str(s)) #描点连线
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.legend()
    plt.title('第%d次迭代'%time,verticalalignment= 'bottom'  ,fontsize=22,y=1)
    plt.annotate(ss, (t - A/B,0), xycoords='data', xytext=(2, 0.5), arrowprops=dict(arrowstyle='->'),fontsize=22)
    # plt.suptitle('Categorical Plotting',y=1)
    # plt.subplots_adjust(top=0.8)
    plt.plot(t - A/B,0,marker = "x",markersize=10)
    plt.savefig(r'C:\Users\南宫问俊\Desktop\test\图片\%d.png'%time)#保存图片
    plt.show() #出图


def Newton(a: List[int], b, c):  # 列表a为一元多项式的各项系数   b为初始点   c为要求得精度,即最后得到的值带入f(x)其小于c
    def polynomial(coefficient, x):  # 定义多项式的乘法
        return reduce(lambda c1, c2: c1 * x + c2, coefficient)

    def f(x):  # 反回函数值
        return polynomial(a, x)

    def maa(s):  # 求导方法
        l = len(s)
        ex = [0 for i in range(l - 1)]
        for i in range(2, l + 1):
            ex[-(i - 1)] = ((i - 1) * s[(-1) * (i)])
        return ex

    go = maa(a)  # 存储中间变量

    def fd(x):  # 求导数的值
        return polynomial(go, x)

    def newtonMethod(n, target):  # 牛顿差值开始迭代
        time = n
        x = target
        Next = 0
        A = f(x)
        B = fd(x)
        plot(time, x, A, B)  # 调用画图函数
        print('第%d次迭代' % time, '\n'  '此时迭代点 = %f' % target, '\n' '迭代点此时斜率 = ' + str(B), '\n' '此时迭代值 = ' + str(A))
        if f(x) == 0.0:
            return time, x
        else:
            Next = x - A / B
            print('下一个迭代点 = ' + str(Next), end='\n\n')
        if abs(A - f(Next)) < c:
            print('\n''满足条件的迭代点为 ' + str(Next), '\t 此时的值为' + str(f(Next)))
            #         '''设置迭代跳出条件，同时输出满足f(x) = 0的x值'''
        else:
            return newtonMethod(n + 1, Next)

    newtonMethod(0, b)  # 自动运行函数

Newton([1,0,-2],3,1e-6)
'''[1,0,1]表示所求多项式为x^2-2
2 表示从2,0点开始迭代
1e-6 表示最后得到数字的精确度
'''