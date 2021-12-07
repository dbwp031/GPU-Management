from django.shortcuts import render
from .models import *
# Create your views here.
import pandas as pd
import pymysql
from makechart.views import home as chart_home
def home(request):
    item = User.objects.all().values()
    df = pd.DataFrame(item)
    id = df.name.tolist()
    password=df["password"].tolist()
    name=df["name"].tolist()
    position=df["position"].tolist()
    num_gpus=df["num_gpus"].tolist()
    
    mydict={
        'id':id,
        'password':password,
        'name':name,
        'position':position,
        'num_gpus':num_gpus,
    }
    print(mydict)
    
    return render(request,'users.html',context=mydict)

def login(request):
    # _id = request.POST['user_id']
    # _pwd = request.POST['pwd']
    # conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
    # curs = conn.cursor()
    # """select *
    #    from getuser_user
    #     where password = (
    #         select password
    #         from getuser_user
    #         where id = _id)"""
    # sql= f"select * from getuser_user where {_pwd}= ( select password from getuser_user where id = {_id})"
    # curs.execute(sql)
    
    # rows = curs.fetchall()
    # print(rows)
    
    # conn.close()
    return render(request,'login.html',)#context=rows)

def show_login_page(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        _id = request.POST['username']
        _pwd = request.POST['password']
        conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
        curs = conn.cursor()
        sql = f"select * from getuser_user where user_id = '{_id}' and password = '{_pwd}'"
        # sql= f"select * from getuser_user where user_id = '{_id}'"# where {_pwd}= ( select password from getuser_user where id = {_id})"
        curs.execute(sql)
        rows = curs.fetchall()
        print("LOGIN DB")
        print(rows)
        if len(rows) == 0:
            conn.close()
            return render(request,'login.html')
        elif len(rows) == 1:
            print("chart")
            conn.close()
            return render(request,'index.html')
        else:
            print("로그인 가능 인원수가 두명 이상입니다.")
        conn.close()
    
    return render(request,'login.html')


def signup(request):
    # print(request)
    # print(request.method)
    if request.method == 'GET':
        # 페이지를 불러올 때
        return render(request, 'signup.html')
    elif request.method == 'POST':
        # 페이지 내에서 POST 발생 시
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']
        
        print(username)
        print(password)
        print(re_password)
 
        return render(request, 'login.html')
    print("hi")
    print(request)