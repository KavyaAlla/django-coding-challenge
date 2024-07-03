from django.urls import path
from movies.views import MovieListView, MovieDetailViewSet

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'), # get all movies
    path('<int:pk>/', MovieDetailViewSet.as_view({'get': 'retrieve',   # GET request to retrieve a movie
        'put': 'update',     # PUT request to update a movie
        'patch': 'partial_update',  # PATCH request for partial update
        'delete': 'destroy'}), name='movie-detail'), # get a movie by id
]


