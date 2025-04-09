from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('DOCTOR', 'Doctor'),
        ('PATIENT', 'Patient'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    specialization = models.CharField(max_length=100, blank=True, null=True)  # For doctors
    license_number = models.CharField(max_length=50, blank=True, null=True)  # For doctors
    date_of_birth = models.DateField(blank=True, null=True)  # For patients
    health_insurance = models.CharField(max_length=100, blank=True, null=True)  # For patients

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
