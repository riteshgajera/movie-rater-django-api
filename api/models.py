from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=50)
    # image = models.ImageField(null=True, blank=True ,upload_to='api/images/')
    image = models.ImageField(upload_to='api/images/')
    description = models.TextField(max_length=300)

    def num_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        ratings = Rating.objects.filter(movie=self)
        if len(ratings) > 0:
            return sum([rating.stars for rating in ratings]) / len(ratings)
        else:
            return 0
        return len(ratings)

    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
