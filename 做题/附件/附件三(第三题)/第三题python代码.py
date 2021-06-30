import matplotlib.pyplot as plt
import xlwt
import math

a=list(range(2022))
y=[]
for i in a:
    y.append(1/((math.e)**(math.log(3/2) - (33*i)/250) + 1))
plt.plot(a,y)
plt.show()

'''画图'''

def write_file():
    book = xlwt.Workbook(encoding='utf-8') #创建Workbook，相当于创建Excel
    # 创建sheet，Sheet1为表的名字，cell_overwrite_ok为是否覆盖单元格
    sheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)

    #向表中添加数据
    for i in range(1,2023):
        sheet1.write(i,0, str(a[i-1]))
    for i in range(1,2023):
        sheet1.write(i,1 , str(y[i-1]))
    sheet1.write(0, 0, '初值')
    sheet1.write(0, 1, '因变值')
    book.save(r'.\logistic模型数据.xls')
write_file()

a=list(range(101))
y=[]
for i in a:
    y.append(1/((math.e)**(math.log(3/2) - (33*i)/250) + 1))
plt.plot(a,y,label='x=1/(exp(log(3/2) - (33*t)/250) + 1)', color='black', markersize=1, linewidth=2)
plt.xlabel('t',fontsize=30)
plt.ylabel('x',fontsize=30)
plt.title('前一百年的模型图')
plt.legend()
plt.xticks(fontproperties='Times New Roman', size=20)
plt.yticks(fontproperties='Times New Roman', size=20)
ax=plt.gca()
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
plt.show()