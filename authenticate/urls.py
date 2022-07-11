from django.urls import path
from .import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('users/', views.show_register_user, name='users'),
    path('login/',views.user_login, name='login'),
    path('logout/', views.user_logout, name="logout"),
    path('profile/',views.user_profile, name="profile"),
    path('update/<int:my_id>/', views.update, name='update'),
    path('delete/<int:my_id>/', views.delete, name='delete'),
]