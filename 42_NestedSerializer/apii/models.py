from django.db import models

# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name= 'sungby')
    # related_name  attribute specifies the name of the reverse relation from the User model back to your mode
    duration = models.IntegerField()

    def __str__(self):
        return self.title
