from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField( validators=[MinValueValidator(8),MaxValueValidator(92)])
    hrate = models.IntegerField(default=60, validators=[MinValueValidator(52),MaxValueValidator(82)])
    
    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()} is {self.age} yrs old."