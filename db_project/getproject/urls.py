from django.urls import path
from getproject import views
from makechart.views import home as chart_home
urlpatterns = [
        path('',views.set_project,name='home_user'),
        path('join_project',views.join_project,name='home_user'),
        path('del_project',views.del_project,name='del_project'),
        path('del_project_user',views.del_project_user,name='del_project_s'),

]
