from django.urls import path
from .views import Index, AddSales, GetSalesById, UpdateSales, DeleteSales


urlpatterns = [
    path('', Index.as_view()),
    path('add', AddSales.as_view()),
    path('get/<int:pk>', GetSalesById.as_view()),
    path('update/<int:pk>', UpdateSales.as_view()),
    path('delete/<int:pk>', DeleteSales.as_view()),
]