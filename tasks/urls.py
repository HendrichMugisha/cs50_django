from django.urls import include, path
from . import views

app_name = "tasks"
urlpatterns =[
    path("", views.index, name='home'),
    path("add_task", views.add_task, name='add_task'),
]