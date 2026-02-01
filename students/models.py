from django.db import models
from django.conf import settings
from departments.models import Department

User = settings.AUTH_USER_MODEL

class Student(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('ACTIVE', 'Active'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    semester = models.PositiveIntegerField(null=True, blank=True)
    batch = models.CharField(max_length=10, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return self.user.username
