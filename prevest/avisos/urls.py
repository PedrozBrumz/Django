from django.urls import path
from .views import register, home, post_aviso, avisos, delete_aviso, manual_logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('post-aviso/', post_aviso, name='post_aviso'),
    path('avisos/', avisos, name='avisos'),
    path('logout/', manual_logout, name='logout'),
    path('delete-aviso/<int:aviso_id>/', delete_aviso, name='delete_aviso'),
]