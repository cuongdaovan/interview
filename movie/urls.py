from django.urls import path

from . import views
from .models import Movie

urlpatterns = [
    path('', views.index, name="movies"),
    path('<pk>/', views.detail, name="detail")
]
