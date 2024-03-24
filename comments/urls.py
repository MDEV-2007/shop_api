from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from comments import views

urlpatterns = [
    path('shop/comments/', views.get_comment),
]

urlpatterns = format_suffix_patterns(urlpatterns)