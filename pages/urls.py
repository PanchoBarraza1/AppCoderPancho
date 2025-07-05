from django.urls import path
from .views import (
    PageListView,
    PageDetailView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
)

urlpatterns = [
    path('', PageListView.as_view(), name='page-list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    path('crear/', PageCreateView.as_view(), name='page-create'),
    path('<int:pk>/editar/', PageUpdateView.as_view(), name='page-update'),
    path('<int:pk>/borrar/', PageDeleteView.as_view(), name='page-delete'),
]
