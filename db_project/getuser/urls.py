from django.urls import path
from getuser import views
from makechart.views import home as chart_home
urlpatterns = [
        path('',views.home,name='home_user'),
        path('user/login',views.show_login_page,name='login_user'),
        path('user/main',chart_home,name='login_success_user'),
        path('user/signup',views.signup,name="user_signup")
        # path('user/login/fail')/
]
