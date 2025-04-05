from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Photo {self.id} - {self.upload_date}"

# Create your models here.
