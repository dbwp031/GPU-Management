from django.urls import path
from getuser import views
urlpatterns = [
        path('',views.home,name='home_user'),
        path('user/login',views.show_login_page,name='login_user'),
        path('user/login/success',views.login,name='login_success_user'),
        
        # path('user/login/fail')/
]
