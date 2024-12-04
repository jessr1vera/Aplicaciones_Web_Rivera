from django.urls import path
from .views import CustomLoginView
from . import views
from .views import IndexView 

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('index/', IndexView.as_view(), name='index'),
    path('productos/crear/', views.ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto_delete'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),
] 
