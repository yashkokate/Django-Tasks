from django.db import models

class MediaQuerySet(models.QuerySet):
    def audio(self):
        return self.filter(media_type='Audio')

    def video(self):
        return self.filter(media_type='Video')

    def image(self):
        return self.filter(media_type='Image')

class MediaManager(models.Manager):
    def get_queryset(self):
        return MediaQuerySet(self.model, using=self._db)

    def audio(self):
        return self.get_queryset().audio()

    def video(self):
        return self.get_queryset().video()

    def image(self):
        return self.get_queryset().image()

class Media(models.Model):
    MEDIA_TYPES = (
        ('Audio', 'Audio'),
        ('Video', 'Video'),
        ('Image', 'Image'),
    )

    name = models.CharField(max_length=255)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    format = models.CharField(max_length=50)
    size_mb = models.DecimalField(max_digits=10, decimal_places=2)
    duration_secs = models.PositiveIntegerField(default=0)

    objects = MediaManager()

    def __str__(self):
        return self.name
