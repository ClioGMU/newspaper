from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import os
import uuid


def uuid_filename(instance, filename):
    ext = filename.split(".")[-1]
    id = uuid.uuid4()
    filename = f"${id}.${ext}"
    return os.path.join("img", filename)


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    pdf = models.FileField(upload_to="pdf/%Y/%m/%d/", null=True)
    featured_img = models.ImageField(upload_to=uuid_filename, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])

