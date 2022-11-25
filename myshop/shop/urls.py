from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path('', views.ProductListView.as_view(), name='master_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='master_detail'),
    path('new/', views.ProductCreateView.as_view(), name='master_new'),
    path('<int:pk>/edit', views.ProductUpdateView.as_view(), name='master_edit'),
    path('<int:pk>/delete', views.ProductDeleteView.as_view(), name='master_delete')
]
