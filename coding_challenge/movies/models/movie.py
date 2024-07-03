from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    runtime = models.IntegerField(default=0)  # in minutes

    def runtime_formatted(self):
        hours = self.runtime // 60
        minutes = self.runtime % 60
        return f"{hours}:{minutes:02d}"

    def __str__(self):
        return self.title
