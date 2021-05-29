from django.urls import path

from adminapp.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView, \
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users-read/', UserListView.as_view(), name='users_read'),
    path('users-create/', UserCreateView.as_view(), name='users_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='users_update'),
    path('users-remove/<int:pk>/', UserDeleteView.as_view(), name='users_remove'),
    path('categories-read/', CategoryListView.as_view(), name='categories_read'),
    path('categories-create/', CategoryCreateView.as_view(), name='categories_create'),
    path('categories-update/<int:pk>/', CategoryUpdateView.as_view(), name='categories_update'),
    path('categories-remove/<int:pk>/', CategoryDeleteView.as_view(), name='categories_remove')
]
