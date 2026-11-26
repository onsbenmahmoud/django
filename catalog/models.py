from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'

    doctor = models.ForeignKey('AccountApp.Doctor', on_delete=models.CASCADE,
                               related_name='appointments')
    patient = models.ForeignKey('AccountApp.Patient', on_delete=models.CASCADE,
                                related_name='appointments')
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    prescription = models.FileField(
        upload_to='prescriptions/', blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
    )
    status = models.CharField(max_length=10, choices=Status.choices,
                              default=Status.PENDING)
    doctor = models.ForeignKey('AccountApp.Doctor', on_delete=models.CASCADE,
                               related_name='appointments')
    patient = models.ForeignKey('AccountApp.Patient', on_delete=models.CASCADE,
                                related_name='appointments')