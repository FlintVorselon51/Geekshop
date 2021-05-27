from django.urls import path

from .views import index, \
    categories_read, categories_create, categories_update, categories_remove
from adminapp.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users-read/', UserListView.as_view(), name='users_read'),
    path('users-create/', UserCreateView.as_view(), name='users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='users_update'),
    path('users-remove/<int:pk>/', UserDeleteView.as_view(), name='users_remove'),
    path('categories-read/', categories_read, name='categories_read'),
    path('categories-create/', categories_create, name='categories_create'),
    path('categories-update/<int:category_id>/', categories_update, name='categories_update'),
    path('categories-remove/<int:category_id>/', categories_remove, name='categories_remove')
]
