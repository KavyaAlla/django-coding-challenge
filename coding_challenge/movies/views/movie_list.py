from rest_framework.generics import ListCreateAPIView
from movies.models import Movie
from movies.serializers.movie_serializer import MovieSerializer

class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.order_by("id")
    serializer_class = MovieSerializer
