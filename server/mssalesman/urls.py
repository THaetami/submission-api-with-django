from django.urls import path
from .views import Index, AddSales, GetSalesById, UpdateSales, DeleteSales


urlpatterns = [
    path('', Index.as_view()),
    path('create', AddSales.as_view()),
    path('<int:pk>', GetSalesById.as_view()),
    path('<int:pk>/update', UpdateSales.as_view()),
    path('<int:pk>/delete', DeleteSales.as_view()),
]