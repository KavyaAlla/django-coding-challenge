from rest_framework.generics import ListCreateAPIView
from movies.models import Movie
from movies.serializers.movie_serializer import MovieSerializer

class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.order_by("id")
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        min_runtime = self.request.query_params.get('min_runtime')
        max_runtime = self.request.query_params.get('max_runtime')

        if min_runtime:
            queryset = queryset.filter(runtime__gt=int(min_runtime))
        if max_runtime:
            queryset = queryset.filter(runtime__lt=int(max_runtime))

        return queryset