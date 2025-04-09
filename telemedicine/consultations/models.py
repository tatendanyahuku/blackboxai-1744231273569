import uuid
from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator
from django.utils import timezone

class Consultation(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='patient_consultations')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='doctor_consultations')
    scheduled_time = models.DateTimeField(validators=[MinValueValidator(timezone.now)])
    duration = models.PositiveIntegerField(help_text="Duration in minutes") 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    symptoms = models.TextField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    room_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    call_duration = models.PositiveIntegerField(default=0, help_text="Duration in seconds")

    def __str__(self):
        return f"Consultation #{self.id} - {self.patient} with {self.doctor}"

    class Meta:
        ordering = ['-scheduled_time']
