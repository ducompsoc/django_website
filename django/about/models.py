from django.db import models


class PageContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
