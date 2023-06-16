from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail')
    ]