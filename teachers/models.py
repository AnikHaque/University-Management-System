from django.db import models
from django.conf import settings
from departments.models import Department

User = settings.AUTH_USER_MODEL

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username
