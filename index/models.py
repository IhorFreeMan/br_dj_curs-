from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title


class Notes(models.Model):
    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title