from django.db import models


class ImageCarousel(models.Model):
    images = models.ManyToManyField('site_wide.Image')
    view = models.CharField(max_length=50, default='')
