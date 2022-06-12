from django.db import models


class Series(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    photo = models.URLField()


class Review(models.Model):
    content = models.TextField()
    series = models.ForeignKey(Series, on_delete=models.CASCADE)


class Suggestions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
