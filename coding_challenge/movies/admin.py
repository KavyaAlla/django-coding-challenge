from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdminConsole(admin.ModelAdmin):
    list_display = ('id', 'title', 'runtime', 'release_date')
    search_fields = ('title', 'release_date')  # Enable search by title and release date
    list_filter = ('release_date',)  # Enable filtering by release date
    date_hierarchy = 'release_date'  # Adds a date drill-down navigation by release date
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'name', 'rating')  # Assuming you have a 'date_posted' field
    search_fields = ('name', 'movie__title')  # Allow searching by reviewer's name and movie title
     # Filter options
