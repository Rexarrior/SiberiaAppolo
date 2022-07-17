from django.db import models as models
class Task1Answer(models.Model):
    guid = models.CharField(max_length=300)
    score = models.FloatField()