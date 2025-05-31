from django.db import models
from django.conf import settings


class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Exercise(models.Model):
    name = models.TextField()
    rest_time = models.FloatField()
    min_reps = models.IntegerField()
    max_reps = models.IntegerField()

class Set(models.Model):
    set_number = models.IntegerField()
    reps = models.FloatField()
    weight = models.FloatField()
