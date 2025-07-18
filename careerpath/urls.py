from django.urls import path
from . import views

urlpatterns = [
    path('', views.career_path, name='career_path'),
    path('subfield/<int:subfield_id>/', views.subfield_detail, name='subfield_detail'),
]