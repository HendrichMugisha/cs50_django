

from django.urls import path
from . import views

app_name = 'mytasks'
urlpatterns = [
    path('', views.mytasks, name='home' ),
    path('add/', views.addtask, name='add' )
]