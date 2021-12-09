from django.shortcuts import render
from .models import *
# Create your views here.
import pymysql
import pandas as pd
import datetime
def set_project(request):
    if request.method == "GET":
        return render(request,'set_project.html')
    elif request.method == "POST":
        project_id = request.POST['project_id']
        partners = request.POST['partners']
        
        conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
        curs = conn.cursor()    
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        print(date)
        sql = f"insert into getproject_project(project_id, partners, details, start_date,end_date, budget) values('{project_id}','{partners}','','{date}','{date}',1)"
        curs.execute(sql)
        rows = curs.fetchall()
        conn.commit()
        print(rows)     
        conn.close()     
        return render(request,'set_project.html')
    
def join_project(request):
    if request.method == "GET":
        return render(request,'join_project.html')
    elif request.method == "POST":
        project_id = request.POST['project_id']
        user_id = request.POST['user_id']
        
        conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
        curs = conn.cursor()    
        sql = f"insert into getproject_project_participants_id(project_id, user_id) values('{project_id}','{user_id}')"        
        curs.execute(sql)
        rows = curs.fetchall()
        conn.commit()
        print(rows)     
        conn.close()     
        return render(request,'join_project.html')

def del_project(request):
    if request.method == "GET":
        return render(request,'del_project.html')
    elif request.method == "POST":
        project_id = request.POST['project_id']
        conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
        curs = conn.cursor()    
        # 관계 테이블 삭제
        
        sql = f"delete from getproject_project_participants_id where project_id = '{project_id}'"
        curs.execute(sql)
        conn.commit()

        # 프로젝트 삭제
        sql = f"delete from getproject_project where project_id = '{project_id}'"
        curs.execute(sql)
        rows = curs.fetchall()
        conn.commit()
        print(rows)     
        conn.close()     
        return render(request,'del_project.html')
    
def del_project_user(request):
    if request.method == "GET":
        return render(request,'del_project_user.html')
    elif request.method == "POST":
        project_id = request.POST['project_id']
        user_id = request.POST['user_id']
        conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
        curs = conn.cursor()    
        # 관계 테이블 삭제
        sql = f"delete from getproject_project_participants_id where project_id = '{project_id}' and user_id = '{user_id}'"
        curs.execute(sql)
        conn.commit()
        conn.close()     
        return render(request,'del_project_user.html')