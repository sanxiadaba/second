from flask import Flask,render_template,request
import datetime
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return '成功了吗?'

@app.route('/index')
def hello():
    return '你好呀'
#通过访问路径,索取用户字符串参数
@app.route('/user/<name>')
def welcom(name):
    return '你好,%s'%name

@app.route('/user/<int:id>')#此外,还有float类型
def welcom2(id):
    return '你好,%d'%id

# @app.route('/')
# def index2():
#     return render_template('index.html')

@app.route('/')
def index2():
    time =datetime.date.today()#普通变量
    name = ['小张','小王','小赵']#列表类型
    task = {'任务':'打扫卫生','时间':'3小时'}#字典类型
    return render_template('index.html',var=time,list = name,task = task)


#表单提交
@app.route('/test/register')
def register():
    return render_template('test/register.html')

#接受表单提交的路由,需要指定methods为POST
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('test/result.html',result = result)




if __name__ == '__main__':
    app.run()
