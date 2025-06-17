from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('inventario/', views.inventario_list, name='inventario_list'),
    path('producto/crear/', views.producto_crear, name='crear_producto'),
    path('editar/<int:pk>/', views.producto_editar, name='editar_producto'),
    path('eliminar/<int:pk>/', views.producto_eliminar, name='eliminar_producto'),
    path('registro/', views.registro_usuario, name='registro'),
    path('configuracion/', views.configuracion_usuario, name='configuracion'),
    path('categoria/crear/', views.categoria_crear, name='crear_categoria'),
    path('logout/', views.logout_view, name='logout'),
]
