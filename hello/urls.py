from django.urls import path
from .  import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('brian', views.brian, name='brian'),
    # path('david', views.david, name='david'),
    path('<str:name>', views.greet, name='greet'),
]