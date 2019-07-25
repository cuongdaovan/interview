from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.http import HttpResponse
from django.conf import settings
import os
import json

from .models import Movie


def index(request):
    movies = Movie.objects.all()
    print(movies)
    return render(request, "movie/index.html", {'movies': movies})


def detail(request, pk):
    movie = Movie.objects.get(id=pk)
    print(movie)
    return render(request, "movie/detail.html", {'movie': movie})
