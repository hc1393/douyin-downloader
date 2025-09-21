from flask import Blueprint, session, redirect, render_template, url_for, flash
from day21.utils import db

od = Blueprint('order', __name__)

@od.route('/order/list',methods=['GET','POST'])
def order_list():
    user_info = session.get('userinfo')
    role = user_info['role']
    print(role)#1-客户,2-管理员
    if role == 2:
        data_list = db.fetch_all("select * from `order` left join userinfo on `order`.user_id = userinfo.id", [])
    else:
        data_list = db.fetch_all("select * from `order` left join userinfo on `order`.user_id = userinfo.id where `order`.user_id=%s", [user_info['id'], ])
    status_dict= {
        1:'待执行',
        2:'正在执行',
        3:'完成',
        4:'失败'
    }
    print(data_list)

    return render_template('order_list.html', data_list=data_list,status_dict=status_dict)


@od.route('/order/create')
def order_create():
    return '创建订单'


@od.route('/order/delete')
def order_delete():
    return '删除订单'
