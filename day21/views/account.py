from flask import Blueprint, render_template, request, redirect
from day21.utils import db

#创建蓝图对象
ac=Blueprint('account',__name__)

@ac.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
       return render_template('login.html')
    #froms
    role=request.form.get('role')
    mobile=request.form.get('mobile')
    pwd=request.form.get('pwd')
    print(role,mobile,pwd)
    #链接数据库查看是否正常
    user_dict=db.fetch_one("select * from hc.userinfo where role=%s and mobile=%s and password=%s",[role,mobile,pwd])
    print(2,user_dict)
    # conn=pymysql.connect(host='127.0.0.1',port=3306,user='roothc',password='root123',charset='utf8',db='hc')
    # cursor=conn.cursor()
    # cursor.execute('select * from userinfo where role=%s and mobile=%s and password=%s',[role,mobile,pwd])
    # user_dict=cursor.fetchone()
    # cursor.close()
    # conn.close()
    if user_dict:
        #登陆成功+跳转
        return redirect('/order/list')
    return render_template('login.html',error='用户名或密码错误')

@ac.route('/users')
def users():
    return '用户列表'

