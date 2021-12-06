from django.shortcuts import render
from .models import *
# Create your views here.
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
    return render(request,'index.html',context=mydict)
