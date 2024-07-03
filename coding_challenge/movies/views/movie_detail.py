from rest_framework import viewsets
from movies.models import Movie
from movies.serializers.movie_serializer import MovieSerializer

class MovieDetailViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
