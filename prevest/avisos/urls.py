from django.urls import path
from .views import register, home, post_aviso, avisos, delete_aviso
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('post-aviso/', post_aviso, name='post_aviso'),
    path('avisos/', avisos, name='avisos'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('delete-aviso/<int:aviso_id>/', delete_aviso, name='delete_aviso'),
]