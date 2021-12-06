from django.urls import path
from makechart import views
urlpatterns = [
        path('',views.home,name='home')  
]
