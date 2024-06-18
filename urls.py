from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('like/<int:post_id>/', views.LikeView, name='like'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]