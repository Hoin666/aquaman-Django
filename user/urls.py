from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('main/', views.main_view, name='main'),
    # 추가 기능을 위한 URL 설정도 여기에 포함될 수 있습니다.
]