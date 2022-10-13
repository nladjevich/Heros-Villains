from django.urls import path
from . import views

urlpatterns = [
    path('', views.supers_list),
    path('<pk>/', views.supers_detail),
]