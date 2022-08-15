from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos', validators=[
                                  FileExtensionValidator(allowed_extensions=['mp4'])])
    thumbnail = models.FileField(upload_to='thumbnails', validators=[
                                 FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
