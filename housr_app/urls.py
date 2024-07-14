from django.urls import path
from .views import property_list, PropertyDetailView, login, logout, register

urlpatterns = [
    path('', property_list, name='property_list'),
    path('property/<int:pk>/', PropertyDetailView.as_view(), name='property_detail'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout')
]