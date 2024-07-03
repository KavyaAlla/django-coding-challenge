from django.contrib import admin
from .models import Movie
from .models import Review

class ReviewInline(admin.TabularInline):  # Using TabularInline for a more compact layout
    model = Review
    extra = 1  # Specifies how many extra forms to display
    fields = ['name', 'rating', 'date_posted']  

@admin.register(Movie)
class MovieAdminConsole(admin.ModelAdmin):
    list_display = ('id', 'title', 'runtime', 'release_date')
    search_fields = ('title', 'release_date')  # Enable search by title and release date
    list_filter = ('release_date',)  # Enable filtering by release date
    date_hierarchy = 'release_date'  # Adds a date drill-down navigation by release date
    inlines = [ReviewInline]  # Add the inline

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'name', 'rating')  # Assuming you have a 'date_posted' field
    search_fields = ('name', 'movie__title')  # Allow searching by reviewer's name and movie title
     # Filter options
    list_filter = ('rating',)