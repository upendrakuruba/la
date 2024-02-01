from django.db import models

# Create your models here.
class Actor(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    remunation=models.IntegerField()
    def __str__(self):
        return self.name