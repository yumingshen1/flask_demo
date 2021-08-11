from flask import Flask,render_template,request
import datetime

app = Flask(__name__)


# @app.route('/')   #路由解析，通过用户访问的路径，匹配相应函数
# def hello_world():
#     return '特么的就是操蛋a 想弄死'


# @app.route('/index')   #路由解析，通过用户访问的路径，匹配相应函数
# def hello_world():
#     return '他不得人心啊'


# @app.route('/user/<name>')   #通过访问路径，获取用户的字符串参数
# def hello_world(name):
#     return '他不得人心啊,%s'%name


# @app.route('/user/<int:id>')   #通过访问路径，获取用户的整型参数
# def welcome(id):
#     return '傻帽%d'%id



## 返回给用户渲染后的网页文件
# @app.route("/")
# def index():
#     return render_template("index.html")

#向页面传递变量
@app.route("/")
def index2():
    data = datetime.date.today()   #普通变量
    name = ['s','b','l']           #列表类型
    book = {"任务":"发财","时间":"会遇到的，别太急"}  #字典
    return render_template("index.html",var = data,n = name,book=book)


#表单提交,  提交页面
@app.route('/test/register')
def biaodan():
    return render_template("test/register.html")

## 表单 。跳转结果页面,  结果页面需要指定可以接受的请求方式
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form      ##如果请求是post那么就将请求的form内容形成字典传给result，
        print('----')
        return render_template('test/result.html',result=result)




if __name__ == '__main__':
    app.run()
'''
ZSPre-K2-11492-14656 -  10:20
ZSPre-K2-11493-14657 -  11:40
ZSPre-K2-11494-14658 -  11:40
'''
