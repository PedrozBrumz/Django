from django.urls import path
from .views import register, home, post_aviso, avisos
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('post-aviso/', post_aviso, name='post_aviso'),
    path('avisos/', avisos, name='avisos'),
]