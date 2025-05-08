from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Quote(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    quote_text = models.TextField(max_length=500)
    quote_author = models.CharField(max_length=100)

    def __str__(self):
        return self.title