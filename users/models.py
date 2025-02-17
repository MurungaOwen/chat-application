from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    """User profile model one that extends attributes of user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.FileField(upload_to='profile-pics', null=True, blank=True)

    def __str__(self):
        """string represetation of the object"""
        return '{}\'s profile'.format(self.user)
    
    # while saving image resize it inplace using pillow
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)