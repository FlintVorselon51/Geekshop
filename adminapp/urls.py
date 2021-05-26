from django.urls import path

from .views import index, users_read, users_create, users_update, users_remove, \
    categories_read, categories_create, categories_update, categories_remove

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('users-read/', users_read, name='users_read'),
    path('users-create/', users_create, name='users_create'),
    path('users-update/<int:user_id>/', users_update, name='users_update'),
    path('users-remove/<int:user_id>/', users_remove, name='users_remove'),
    path('categories-read/', categories_read, name='categories_read'),
    path('categories-create/', categories_create, name='categories_create'),
    path('categories-update/<int:category_id>/', categories_update, name='categories_update'),
    path('categories-remove/<int:category_id>/', categories_remove, name='categories_remove')
]
