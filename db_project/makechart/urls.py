from django.urls import path
from makechart import views
urlpatterns = [
        path('',views.home,name='home'),
        path('get_gpu',views.get_gpu_view,name='get_gpu_view'),  
        path('show_gpu',views.show_gpu_view,name='show_gpu'),
        path('request_gpu',views.get_gpuRequest_view,name='request_gpu'),
        path('show_gpu_byID',views.show_gpu_view_byID,name='show_gpu_byID'),
        path('show_status',views.show_status,name="show_status"),
        path('del_gpu',views.del_gpus,name='delete_gpu'),
        path('del_gpuRequest',views.del_gpuRequest,name='delete_gpuRequest'),

]
