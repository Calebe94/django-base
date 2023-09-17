from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def number_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def average_rating(self):
        sum = 0
        avg = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += int(rating.stars)

        if len(ratings) > 0:
            avg = sum / len(ratings)
        else:
            avg = 0

        return avg

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'))
        index_together = (('user', 'movie'))
