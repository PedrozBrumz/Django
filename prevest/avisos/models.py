from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    coordenador = models.BooleanField(default=False)
    professor = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Aviso(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title