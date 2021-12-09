from django.shortcuts import render
from .models import *
# Create your views here.
import pymysql
import pandas as pd

def home(request):
    item = Student.objects.all().values()
    df = pd.DataFrame(item)
    df1 = df.name.tolist()
    df=df['rank'].tolist()
    mydict={
        'df':df,
        'df1':df1
    }
    print(mydict)
    print(request)
    return render(request,'index.html',context=mydict)

def get_gpu_view(request):
    if request.method == "GET":
        return render(request,'get_gpu.html')
    elif request.method == "POST":
        gpu_id = request.POST['gpu_id']
        gpu_type = request.POST['gpu_type']
        location = request.POST['location']
        vendor = request.POST['vendor']
        
        conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
        curs = conn.cursor()            
        sql = f"insert into makechart_gpu(gpu_id, tpe, location, vendor) values('{gpu_id}','{gpu_type}','{location}','{vendor}')"
        curs.execute(sql)
        conn.commit()
        conn.close()
        return render(request,'get_gpu.html')

def show_gpu_view(request):
    conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
    curs = conn.cursor()
    # 모든 gpu type 불러오기(distinct)
    sql = f"select distinct tpe from makechart_gpu"
    curs.execute(sql)
    gpu_types = [i[0] for i in curs.fetchall()]
    print("df",gpu_types)
    result = {}
    result['df'] = gpu_types
    num_gpus = []
    for t in gpu_types:
        sql = f"select count(*) from makechart_gpu where tpe = '{t}' "
        curs.execute(sql)
        
        num_gpus.append(curs.fetchall()[0][0])
    result['df1']=num_gpus 
    print(num_gpus)
    print(request)
    print(result)
    return render(request,'show_gpu.html',context=result)

def get_gpuRequest_view(request):
    if request.method == "GET":
        return render(request,'request_gpu.html')
    elif request.method == "POST":
        gpu_id = request.POST['gpu_id']
        user_id = request.POST['user_id']
        
        conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
        curs = conn.cursor()            
        sql = f"update makechart_gpu set gpu_users_id='{user_id}' where gpu_id = '{gpu_id}'"
        curs.execute(sql)
        conn.commit()
        conn.close()
        return render(request,'request_gpu.html')
    
def show_gpu_view_byID(request):
    conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
    curs = conn.cursor()
    # 모든 gpu type 불러오기(distinct)
    # sql = f"select distinct tpe from makechart_gpu"
    sql = f"select distinct user_id from getuser_user"
    curs.execute(sql)
    gpu_types = [i[0] for i in curs.fetchall()]
    print("df",gpu_types)
    result = {}
    result['df'] = gpu_types
    num_gpus = []
    for t in gpu_types:
        sql = f"select count(*) from makechart_gpu where gpu_users_id = '{t}' "
        curs.execute(sql)
        
        num_gpus.append(curs.fetchall()[0][0])
    result['df1']=num_gpus 
    print(num_gpus)
    print(request)
    print(result)
    return render(request,'show_gpu.html',context=result)

def show_status(request):
    conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
    curs = conn.cursor()
    # gpu 총 개수
    sql = f"select count(*) from makechart_gpu"
    curs.execute(sql)
    all_gpus = curs.fetchall()[0][0]
    # 사용 gpu 개수
    sql = f"select count(*) from makechart_gpu where gpu_users_id is not null"
    curs.execute(sql)
    used_gpus = curs.fetchall()[0][0]
    result={}
    index= ['used_gpus','remained_gpus']
    value = [used_gpus,all_gpus-used_gpus]
    result['df']=index
    result['df1']=value
    ########################
    sql = f"select distinct user_id from getproject_project_participants_id"
    curs.execute(sql)
    participants = [i[0] for i in curs.fetchall()]
    num_projects=[]
    for t in participants:
        sql = f"select count(*) from getproject_project_participants_id where user_id = '{t}' "
        curs.execute(sql)
        num_projects.append(curs.fetchall()[0][0])
    result['participants'] = participants
    result['num_projects'] = num_projects
    print(result)
    return render(request,'show_status.html',context=result)

def del_gpus(request):
    if request.method == "GET":
        return render(request,'del_gpu.html')
    elif request.method == "POST":
        gpu_id = request.POST['gpu_id']
        
        conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
        curs = conn.cursor()            
        sql = f"delete from makechart_gpu where gpu_id = '{gpu_id}'"
        curs.execute(sql)
        conn.commit()
        conn.close()
        return render(request,'del_gpu.html')


def del_gpuRequest(request):
    if request.method == "GET":
        return render(request,'del_gpuRequest.html')
    elif request.method == "POST":
        gpu_id = request.POST['gpu_id']
        user_id = request.POST['user_id']
        
        conn = pymysql.connect(host='127.0.0.1',user='root',password='!Yooje1207',db='db_project',charset='utf8')
        curs = conn.cursor()            
        sql = f"update makechart_gpu set gpu_users_id = NULL where gpu_id = '{gpu_id}' and gpu_users_id = '{user_id}'"
        curs.execute(sql)
        conn.commit()
        conn.close()
        return render(request,'del_gpuRequest.html')