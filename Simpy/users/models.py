from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Photo', default=None, upload_to='user_images')

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'
