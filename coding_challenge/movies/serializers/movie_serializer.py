from rest_framework import serializers
from movies.models import Movie
from .review_serializer import ReviewSerializer

class MovieSerializer(serializers.ModelSerializer):
    reviewers = ReviewSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    runtime_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'runtime', 'runtime_formatted', 'reviewers', 'avg_rating']

    def get_avg_rating(self, obj):
        reviews = obj.reviews.all()
        if not reviews.exists():
            return 0
        return sum(review.rating for review in reviews) / reviews.count()

    def get_runtime_formatted(self, obj):
        hours = obj.runtime // 60
        minutes = obj.runtime % 60
        return f"{hours}:{minutes:02d}"
