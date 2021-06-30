import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

x=np.linspace(0,1,1000) #构造横坐标数据
zh=[]
for i in x:
    zh.append(math.cos(i))
zh=np.array(zh)
y=(math.e)**(zh)
plt.plot(x,y,label='y=e^(cos(x))', color='g', markersize=1, linewidth=2) #描点连线
plt.title('e^(cos(x))的函数图像',size=20)
plt.xlabel('x',fontsize=20)
plt.ylabel('y',fontsize=20)
plt.legend()
plt.xticks(fontproperties='Times New Roman', size=20)
plt.yticks(fontproperties='Times New Roman', size=20)
ax=plt.gca()
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
# with pysnooper.snoop():
for i in range(1000):
    if i%100==0:
        plt.vlines(x[i], 0, y[i], linestyles ="--", colors ="k", linewidth=0.7)
    else:
        continue
plt.vlines(1.0, 0, ((math.e)**(math.cos(1))), linestyles ="--", colors ="k", linewidth=1.7)
plt.vlines(0, 0, ((math.e)**(math.cos(0))), linestyles ="--", colors ="k", linewidth=1.7)
plt.hlines(0, 0, 1, linestyles ="--", colors ="k", linewidth=1.7)
plt.text(0.35, 1.1, "面积", size = 35, alpha = 0.8)
plt.show()

import math
import random

upper_bound = 1  # 积分上界
lower_bound = 0  # 积分下界


def f(x):  # 定义原函数
    return (math.e) ** (math.cos(x))


sum = 0
count = 1
while count <= 1e+4:  # 为了方便,这里模拟一万个点
    sum = sum + f(random.uniform(lower_bound, upper_bound))  # 在积分区间里生成随机数,并且都加起来
    count = count + 1  # 计算点的个数
MonteCarloMethod = (upper_bound - lower_bound) * (sum / 10000)
# 模拟情况
print("用蒙特卡洛方法计算的定积分：")
print(MonteCarloMethod)
