from django.db import models

# Create your models here.

class Receipebook(models.Model):
    receipename=models.CharField(max_length=100)
    receipedesc=models.TextField()
    receipeimg=models.FileField(upload_to= 'receipes/')

    def __str__(self):
        return f"{self.receipename}"