from django.db import models
from PIL import Image
import os

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Image field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)

            # Resize maintaining aspect ratio (max 300x300)
            img.thumbnail((300, 300))

            # Save in original format or JPEG if not specified
            format = img.format if img.format else 'JPEG'
            if format.upper() == 'JPEG':
                img.save(img_path, format=format, quality=80, optimize=True)
            else:
                img.save(img_path, format=format)