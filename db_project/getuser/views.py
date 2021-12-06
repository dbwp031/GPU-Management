from django.shortcuts import render
from .models import *
# Create your views here.
import pandas as pd
import pymysql
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
    return render(request,'login.html')
