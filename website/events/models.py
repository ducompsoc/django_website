from django.db import models
from django.utils import timezone

def image_upload_path_handler(instance, filename):
    # pk chosen because can't be sure that title will be nice to use as a path
    return "events/static/events/img/{0}_{1}.jpg".format(instance.pk, timezone.now())

class Event(models.Model):
    title = models.CharField(max_length=100)
    # ie. for scheduling when an event is made visible on the website
    publication_datetime = models.DateTimeField("Expected publication date and time")
    content = models.CharField(max_length=1000)
    event_datetime = models.DateTimeField("Time and date of the event")
    image = models.ImageField(upload_to=image_upload_path_handler)

    # Because pk is not known at image save time, save the model with empty image, then overwrite
    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.image
            self.image = None
            super(Event, self).save(*args, **kwargs)
            self.image = saved_image

        super(Event, self).save(*args, **kwargs)
