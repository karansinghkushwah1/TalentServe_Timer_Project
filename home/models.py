from django.db import models

# Create your models here.

# my changes 
from django.contrib.auth.models import User
from datetime import datetime



# class UserActivity(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     login_time = models.DateTimeField(default=timezone.now)
#     logout_time = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return self.user.username

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=datetime.now)
    logout_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username
