from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', verbose_name="Autor", on_delete=models.CASCADE)
    title = models.CharField("Título", max_length=255)
    text = models.TextField("Texto", max_length=1024)
    created_at = models.DateTimeField("Data de criação", auto_now=True)

    def __str__(self):
        return self.title
