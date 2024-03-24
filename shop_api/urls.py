from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shop_api import views

urlpatterns = [
    path('shop/', views.shop_list),
    path('shop/<int:pk>/', views.shop_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)