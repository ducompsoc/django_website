from django.db import models
from django.utils import timezone


def image_upload_path_handler(instance, filename):
    # pk chosen because can't be sure that title will be nice to use as a path
    return "website/img/{0}_{1}.jpg".format(instance.pk, timezone.now())


class Image(models.Model):
    image = models.ImageField(upload_to=image_upload_path_handler)

    # Because pk is not known at image save time, save the model with empty image, then overwrite
    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.image
            self.image = None
            super(Image, self).save(*args, **kwargs)
            self.image = saved_image

        super(Image, self).save(*args, **kwargs)
