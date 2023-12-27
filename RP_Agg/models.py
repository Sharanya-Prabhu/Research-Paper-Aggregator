from django.db import models
from django.contrib.auth.models import User

class Paper(models.Model):
    title = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='papers')

    def __str__(self):
        return self.title


class UserPaperPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.ManyToManyField(Paper)

    def __str__(self):
        return self.user.username

