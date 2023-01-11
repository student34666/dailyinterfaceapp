from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField()

    def __str__(self) -> str:
        return f"{self.user.username} Profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
