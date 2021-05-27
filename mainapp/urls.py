from django.urls import path

from .views import ProductsView

app_name = 'mainapp'

urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('<int:category_id>/', ProductsView.as_view(), name='product'),
    path('page/<int:page>/', ProductsView.as_view(), name='page')
]
