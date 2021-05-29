from django.urls import path

from .views import login, logout, profile, CreateUserView

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('profile/', profile, name='profile')
]
