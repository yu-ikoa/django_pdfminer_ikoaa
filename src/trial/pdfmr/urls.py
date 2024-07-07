from django.contrib import admin
from django.urls import path
from . import views

app_name = "pdfmr"

urlpatterns = [
    path('top/', views.top, name='top'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('list/', views.ListView.as_view(), name='list'),
    path('dell_file/', views.dell_file, name='dell_file'),
]