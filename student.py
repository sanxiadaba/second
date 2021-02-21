filename='student.txt'
import os
def menu():
    print('____________________学生成绩管理信息____________________')
    print('_______________________功能列表_______________________')
    print('1.录入学生信息')
    print('2.查找学生信息')
    print('3.删除学生信息')
    print('4.修改学生信息')
    print('5.对学生成绩排序')
    print('6.统计总人数')
    print('7.显示所有学生信息')
    print('0.退出系统')
    print('_____________________________________________________')

def insert():
    while True:
        c=[]
        d=[]
        with open(filename,'a',encoding='utf-8') as gr:
            pass
        fr = open(filename,'r+',encoding='utf-8')
        size = os.path.getsize(filename)
        if size == 0:
            try:
                id = int(input('请输入id(数字):\n'))
                if id=='':
                    print('输入格式不合规范!!!\n')
                if not id:
                    print('输入格式不合规范!!!\n')
                    break
            except:
                print('输入格式不合规范!!!\n')
                break
        else:
            a=fr.readlines()
            for i in a:
                b=dict(eval(i))
                c.append(b)
            try:
                id=int(input('请输入id(数字):\n'))
                if not id:
                    print('输入格式不合规范!!!\n')
                    break
            except:
                print('输入格式不合规范!!!\n')
                break

            for item1 in c:
                for item2 in  item1:
                    d.append(item1['id'])
        if id in d:
            print('该生成绩已输入!!!')
            break

        name = str(input(('输入name:\n')))
        if not name:
            print('输入格式不合规范!!!')
            break
        try:
            English = int(input('输入英语成绩:\n'))
            Python = int(input('输入Python成绩:\n'))
            Java = int(input('输入Java成绩:\n'))
            if English < 0 or Python < 0 or Java < 0:
                print('输入信息格式错误!!!')
                break
        except:
            print('录入信息格式错误!!!\n')
            break
        stu = {'id': id, 'name': name, '英语': English, 'Python': Python, 'Java': Java}
        answer = str(input('是否继续添加? y/n\n'))
        if answer == 'n' or answer == 'N':
            add(stu)
            print('学生系统录入完毕!!!\n')
            break
        if answer == 'y' or answer == 'Y':
            add(stu)
            continue
        else:
            break

def add(lst):
    with open(filename,'a+',encoding='utf-8') as fw:
        fw.write(str(lst)+'\n')

def scr(a):
    b='{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    print(b.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    c='{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for i in a:
        print(c.format(i.get('id'),i.get('name'),i.get('英语'),i.get('Python'),i.get('Java'),int(int(i.get('英语'))+int(i.get('Python'))+int(i.get('Java')))))
    return

def search():
    while True:
        f=[]
        l=[]
        sd=[]
        if judge(filename)==1:
            break
        else:
            with open(filename, 'r', encoding='utf-8') as b:
                c = b.readlines()
            a=int(input('按id查询(1)还是按姓名查询(2)?\n'))
            if a==1:
                try:
                    d=int(input('输入你要查询的id:\n'))
                    if not d:
                        print('输入格式不对!!!\n')
                        continue
                    else:
                        for p in c:
                            e=dict(eval(p))
                            f.append(e['id'])
                        if d in f:
                            for z in c:
                                y=dict(eval(z))
                                if y['id']==d:
                                    sd.append(y)
                            print(f'id为{d}的成绩如下:\n')
                            scr(sd)
                            try:
                                v=str(input('是否要继续查询? y/n\n'))
                                if v == 'y' or v == 'y':
                                    continue
                                else:
                                    break
                            except:
                                print('输入格式有问题!!!\n')
                                break
                        else:
                            print(f'没有学号为{d}的信息,请先录入!!!')
                            break
                except:
                    pass
            elif a==2:
                try:
                    g = str(input('输入你要查询的姓名:\n'))
                except:
                    print('输入格式有误!!!\n')
                for j in c:
                    k=dict(eval(j))
                    l.append(k['name'])
                if g in l:
                    for d in c:
                        h=dict(eval(d))
                        if h['name']==g:
                            sd.append(h)
                    print(f'姓名为{g}的成绩如下:\n')
                    scr(sd)
                    try:
                        v = str(input('是否要继续查询? y/n'))
                        if v == 'y' or v == 'y':
                            continue
                        else:
                            break
                    except:
                        print('输入格式有问题!!!\n')
                        break
            else:
                print('输入格式错误!!!\n')
                break

def delete():
    while True:
        c=[]
        if judge(filename)==1:
            break
        else:
            try:
                b=int(input('输入你想要删除的id:\n'))
                if not b:
                    print('请输入规范的格式!!!\n')
                    break
            except:
                print('输入格式有问题!!!\n')
                break
            with open(filename, 'r', encoding='utf-8') as fr:
                a = fr.readlines()
            for l in a:
                d=dict(eval(l))
                for i in d:
                        c.append(d[i])
            if b not in c:
                print(f'您想找的学号为{b}的学生信息未录入!!!\n')
                break
            else:
                x=str(input(f'确定要删除学号为{b}的学生信息吗?  y/n\n'))
                try:
                    if x=='y'or x=='Y':
                        with open('student.txt', 'r+') as file:
                            file.truncate(0)
                        for k in a:
                            e = dict(eval(k))
                            if e['id']!=b:
                                add(e)
                        print('信息已删除!!!')
                        f = str(input('是否继续删除? y/n\n'))
                        if f == 'y' or f == 'Y':
                            continue
                        else:
                            show()
                            break
                    else:
                        show()
                        break
                except:
                        print('输入格式不规范!!!\n')
                        break

def judge(a):
    size = os.path.getsize(a)
    if size == 0:
        print('文件中没有信息,请先执行录入操作!!!\n')
        return 1
    else:
        return 2

def modify():
    z=0
    d=[]
    while True:
        if judge(filename)==1:
            break
        else:
            try:
                a=int(input('输入你要修改的id:\n'))
                if not a:
                    print('请输入正确的格式!!!')
                else:
                    pass
            except:
                print('请输入正确的格式!!!')
        with open(filename,'r',encoding='utf-8') as fr:
            b=fr.readlines()
        for i in b:
            c=dict(eval(i))
            for j in c:
                d.append(c['id'])
        if a not in d:
            print(f'您要修改的{a}未录入!!!\n')
            break
        else:
            with open("student.txt", 'r+') as file:
                file.truncate(0)
            for i in b:
                c = dict(eval(i))
                if c['id']!=a:
                    add(c)
                    continue
                else:
                    u=c
                    z=1
        if z==1:
            print('开始修改\n')
            while True:
                u['name']=input('输入新姓名:\n')
                u['英语']=input('输入新英语成绩:\n')
                u['Python'] = input('输入新的Python成绩:\n')
                u['Java'] = input('输入新的Java成绩:\n')
                add(u)
                x=str(input('修改成功,是否继续修改?y/n\n'))
                try:
                    if x=='y' or x=='y':
                        flag=True
                        break
                    else:
                        flag=False
                        break
                except:
                    print('输入格式有问题!!!')
                    flag=False
                    continue
            else:
                break
        if flag:
            continue
        else:
            break

def sort():
    while True:
        if judge(filename)==1:
            break
        else:
            show()
            try:
                a=int(input('降序排列(1)还是升序排列(2)?\n'))
                if a==1:
                    flag=True
                else:
                    flag=False
            except:
                print('输入格式错误!!!')
            try:
                op=[]
                with open(filename,'r',encoding='utf-8') as yyy:
                    xx=yyy.readlines()
                for i in xx:
                    dd=dict(eval(i))
                    op.append(dd)
                b=int(input('按什么排序? (1.英语成绩;2.Python成绩;3.Java成绩;4.总成绩)\n'))
                if b==1:
                    op.sort(key=lambda x :int(x['英语']),reverse=flag)
                if b == 2:
                    op.sort(key=lambda x :int(x['Python']),reverse=flag)
                if b==3:
                    op.sort(key=lambda x :int(x['Java']),reverse=flag)
                if b == 4:
                    op.sort(key=lambda x :int(x['英语'])+int(x['Python'])+int(x['Java']),reverse=flag)
            except:
                print('输入格式错误!!!')
                break
            scr(op)
            try:
                v = str(input('是否要继续排序? y/n\n'))
                if v == 'y' or v == 'y':
                    continue
                else:
                    break
            except:
                print('输入格式有问题!!!')
                break

def total():
    while True:
        cc=[]
        if judge(filename)==1:
            break
        else:
            with open(filename,'r',encoding='utf-8') as aa:
                bb=aa.readlines()
            for i in  bb:
                s=dict(eval(i))
                cc.append(s)
            d=len(cc)
            print(f'学生总人数为:{d}\n')
            break

def show():
    while True:
        if judge(filename)==1:
            break
        else:
            f = []
            with open(filename,'r',encoding='utf-8') as a:
                b=a.readlines()
            for i in b:
                ko=dict(eval(i))
                f.append(ko)
            scr(f)
            break

def main():
     while True:
        menu()
        print()
        try:
            a = int(input('输入你要进行的操作的编号:\n'))
            if a==1:
                insert()
            if a==2:
                search()
            if a==3:
                delete()
            if a==4:
                modify()
            if a==5:
                sort()
            if a==6:
                total()
            if a==7:
                show()
            if a==0:
                b=input('您是要退出吗?y/n\n')
                if b=='y'or b=='Y':
                    print('系统已退出!!!')
                    break
            if a not  in  [0,1,2,3,4,5,6,7]:
                print('输入格式有误,请重新输入!!!\n')
                continue
        except:
            print('输入格式有误,请重新输入!!!\n')
            continue




if __name__ == '__main__':
    try:
        stu2 = open(filename,'r',encoding='utf-8')
    except:
        stu2 = open(filename, 'w', encoding='utf-8')
    main()





    
    
    
    
    
    

