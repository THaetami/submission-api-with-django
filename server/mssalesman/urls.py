from django.urls import path
from .views import Index, AddSales, GetSalesById, UpdateSales, DeleteSales


urlpatterns = [
    path('', Index.as_view()),
    path('create', AddSales.as_view()),
    path('<str:pk>', GetSalesById.as_view()),
    path('<str:pk>/update', UpdateSales.as_view()),
    path('<str:pk>/delete', DeleteSales.as_view()),
]