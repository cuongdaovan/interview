import os
import json
from django.core.management.base import BaseCommand
from django.conf import settings

from movie.models import Movie


class Command(BaseCommand):
    def import_movie(self):
        data_file = open(os.path.join(settings.BASE_DIR, 'movies.json'))
        data = json.loads(data_file.read())
        for movie_data in data:
            title = movie_data.get('Title', None)
            runtime = movie_data.get("Runtime", None)
            language = movie_data.get("Language", None)
            gens = movie_data.get("Genre", None)
            genre = ""
            for g in gens:
                genre += g + ","
            rating = movie_data.get("imdbRating", None)
            image = movie_data.get("Poster", None)
            try:
                movie, created = Movie.objects.get_or_create(
                    title=title,
                    runtime=runtime,
                    language=language,
                    genre=genre,
                    rating=rating,
                    image=image
                )
                if created:
                    movie.save()
                    print("success"+title)
            except Exception as e:
                print("fail: " + str(e))

    def handle(self, *args, **kwargs):
        self.import_movie()
