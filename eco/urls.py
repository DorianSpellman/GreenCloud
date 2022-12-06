from django.urls import path, re_path

from .views import * # из текущего пакета импортируем все ф-ии представления
from users import views as user_views

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', infopage, name='info'), # http://127.0.0.1:8000/
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('codes/', codespage, name='codes'), # http://127.0.0.1:8000/codes/
    path('map/', mappage, name='map'), # http://127.0.0.1:8000/map/
    path('codes/<slug:type_name>/', type, name='type'),
    
]

